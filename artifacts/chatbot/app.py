import os
import base64
from typing import List, Dict

import streamlit as st
from openai import OpenAI

from knowledge import retrieve_relevant, format_context, TOPIC_INDEX

try:
    import tiktoken
    _ENC = tiktoken.get_encoding("o200k_base")

    def count_tokens(text: str) -> int:
        return len(_ENC.encode(text or ""))
except Exception:
    def count_tokens(text: str) -> int:
        return max(1, len((text or "")) // 4)


CHAT_MODEL = "gpt-5.4"
SUMMARY_MODEL = "gpt-5-mini"
TTS_MODEL = "gpt-audio-mini"

KEEP_RECENT_MESSAGES = 2

VOICES = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

ASSISTANT_NAME = "ChatAssist"

BASE_SYSTEM_PROMPT = f"""You are {ASSISTANT_NAME}, the official virtual assistant for Spinneys Lebanon (spinneyslebanon.com), an online grocery store.

Your job is to help shoppers with questions about accounts, orders, delivery, payments, products, the mobile app, loyalty rewards, gift cards, refunds, and contacting the store.

Rules:
- Answer ONLY using the FAQs and store information provided in this prompt or in the conversation. Do NOT invent policies, prices, hours, phone numbers, URLs, email addresses, or product details.
- If a user's question is not covered, say you don't have that specific information and direct them to the Call Center at 1521 (10am-10pm, 7 days a week) or the Contact Us page: https://www.spinneyslebanon.com/default/contact/.
- Be friendly, concise, and clear. Prefer short paragraphs and bullet points.
- When a relevant store section URL is provided in context, include it as a link so the user can go straight to the right page.
- Quote prices, percentages, phone numbers, and addresses verbatim from the provided context.
- Do not discuss topics unrelated to Spinneys Lebanon. Politely redirect.

Top-level store sections you can refer customers to:
{TOPIC_INDEX}
"""


@st.cache_resource
def get_client() -> OpenAI:
    base_url = os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL")
    api_key = os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY")
    if not base_url or not api_key:
        raise RuntimeError(
            "Missing AI integration env vars. "
            "AI_INTEGRATIONS_OPENAI_BASE_URL and "
            "AI_INTEGRATIONS_OPENAI_API_KEY must be set."
        )
    return OpenAI(base_url=base_url, api_key=api_key)


def init_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages: List[Dict[str, str]] = []
    if "summary" not in st.session_state:
        st.session_state.summary: str = ""
    if "tokens_saved" not in st.session_state:
        st.session_state.tokens_saved: int = 0
    if "summarizations" not in st.session_state:
        st.session_state.summarizations: int = 0
    if "tts_enabled" not in st.session_state:
        st.session_state.tts_enabled: bool = True
    if "voice" not in st.session_state:
        st.session_state.voice: str = "nova"


def total_message_tokens(messages: List[Dict[str, str]]) -> int:
    return sum(count_tokens(m.get("content", "")) for m in messages)


def build_api_messages(user_input: str) -> List[Dict[str, str]]:
    """Build the message list to send to the model.

    Includes:
      - The base ChatAssist persona + topic index
      - Any running summary of older turns (memory optimization)
      - Retrieved FAQ snippets relevant to the current user input
      - The recent message buffer (already includes the new user message)
    """
    sys_content = BASE_SYSTEM_PROMPT

    if st.session_state.summary:
        sys_content += (
            "\n\nSummary of earlier conversation (treat as prior context):\n"
            f"{st.session_state.summary}"
        )

    retrieved = retrieve_relevant(user_input, top_n=5)
    context_block = format_context(retrieved)
    if context_block:
        sys_content += (
            "\n\nUse the following knowledge base entries to answer the "
            "user's latest message. Prefer this information over your own "
            "guesses:\n"
            f"{context_block}"
        )

    api_messages: List[Dict[str, str]] = [
        {"role": "system", "content": sys_content}
    ]
    for m in st.session_state.messages:
        api_messages.append({"role": m["role"], "content": m["content"]})
    return api_messages


def maybe_summarize(client: OpenAI) -> None:
    """Always condense any messages older than the most recent turn into
    the running summary and drop them from the buffer."""
    msgs = st.session_state.messages
    if len(msgs) <= KEEP_RECENT_MESSAGES:
        return

    older = msgs[:-KEEP_RECENT_MESSAGES]
    recent = msgs[-KEEP_RECENT_MESSAGES:]

    transcript_lines = []
    for m in older:
        role = "Customer" if m["role"] == "user" else "ChatAssist"
        transcript_lines.append(f"{role}: {m['content']}")
    transcript = "\n".join(transcript_lines)

    summary_instruction = (
        "You compress chat history for a Spinneys Lebanon support assistant. "
        "Update the running summary so it captures everything important from "
        "the prior summary plus the new transcript: customer goals, order "
        "details mentioned, account info shared, decisions, open questions, "
        "and any names/IDs that may matter later. Be dense and factual. "
        "Aim for under 250 words. Output only the new summary, no preamble."
    )

    user_block = ""
    if st.session_state.summary:
        user_block += (
            "Previous summary:\n"
            f"{st.session_state.summary}\n\n"
        )
    user_block += f"New transcript to fold in:\n{transcript}"

    older_tokens = total_message_tokens(older)

    try:
        resp = client.chat.completions.create(
            model=SUMMARY_MODEL,
            max_completion_tokens=600,
            messages=[
                {"role": "system", "content": summary_instruction},
                {"role": "user", "content": user_block},
            ],
        )
        new_summary = (resp.choices[0].message.content or "").strip()
        if new_summary:
            st.session_state.summary = new_summary
            st.session_state.messages = recent
            new_summary_tokens = count_tokens(new_summary)
            saved = max(0, older_tokens - new_summary_tokens)
            st.session_state.tokens_saved += saved
            st.session_state.summarizations += 1
    except Exception as e:
        st.warning(f"Could not summarize history this turn: {e}")


def stream_assistant_reply(client: OpenAI, user_input: str, placeholder) -> str:
    api_messages = build_api_messages(user_input)
    full = ""
    try:
        stream = client.chat.completions.create(
            model=CHAT_MODEL,
            max_completion_tokens=8192,
            messages=api_messages,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content if chunk.choices else None
            if delta:
                full += delta
                placeholder.markdown(full)
    except Exception as e:
        full = f"Sorry, I hit an error generating a reply: {e}"
        placeholder.markdown(full)
    return full


def synthesize_speech(client: OpenAI, text: str, voice: str) -> bytes | None:
    if not text.strip():
        return None
    try:
        completion = client.chat.completions.create(
            model=TTS_MODEL,
            modalities=["text", "audio"],
            audio={"voice": voice, "format": "mp3"},
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a text-to-speech engine. Read the user's "
                        "message aloud verbatim, in a natural conversational "
                        "tone. Do not add, omit, paraphrase, translate, or "
                        "comment on anything."
                    ),
                },
                {"role": "user", "content": text},
            ],
        )
        audio = completion.choices[0].message.audio
        if not audio or not getattr(audio, "data", None):
            return None
        return base64.b64decode(audio.data)
    except Exception as e:
        st.warning(f"Text-to-speech failed: {e}")
        return None


def render_sidebar() -> None:
    with st.sidebar:
        st.header("Settings")

        st.session_state.tts_enabled = st.toggle(
            "Read replies aloud",
            value=st.session_state.tts_enabled,
            help="Generates an audio version of each new reply.",
        )
        st.session_state.voice = st.selectbox(
            "Voice",
            VOICES,
            index=VOICES.index(st.session_state.voice),
            disabled=not st.session_state.tts_enabled,
        )

        st.divider()
        st.subheader("Memory")
        buffer_tokens = total_message_tokens(st.session_state.messages)
        summary_tokens = count_tokens(st.session_state.summary)
        st.metric("Recent buffer (msgs)", len(st.session_state.messages))
        st.metric("Recent buffer (~tokens)", buffer_tokens)
        st.metric("Summary (~tokens)", summary_tokens)
        st.metric("Tokens saved by summarization",
                  st.session_state.tokens_saved)
        st.caption(f"Summarizations run: {st.session_state.summarizations}")

        if st.session_state.summary:
            with st.expander("Current running summary"):
                st.write(st.session_state.summary)

        st.divider()
        st.caption(
            "Trained on Spinneys Lebanon FAQs covering accounts, orders, "
            "delivery, payments, refunds, the mobile app, loyalty rewards, "
            "and gift cards."
        )

        if st.button("Clear conversation", use_container_width=True):
            st.session_state.messages = []
            st.session_state.summary = ""
            st.session_state.tokens_saved = 0
            st.session_state.summarizations = 0
            st.rerun()


def render_history() -> None:
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
            if m["role"] == "assistant" and m.get("audio"):
                st.audio(m["audio"], format="audio/mp3")


SUGGESTED_PROMPTS = [
    "How do I cancel an order?",
    "What payment methods do you accept?",
    "How do I earn loyalty points?",
    "Can I talk to a real person?",
]


def main() -> None:
    st.set_page_config(page_title=ASSISTANT_NAME, layout="centered")
    st.markdown(
        """
        <style>
        .chatassist-header {
            background-color: #FFD200;
            color: #1a1a1a;
            padding: 1.25rem 1.5rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        }
        .chatassist-header h1 {
            margin: 0;
            font-size: 2rem;
            font-weight: 800;
            color: #1a1a1a;
        }
        .chatassist-header p {
            margin: 0.35rem 0 0 0;
            font-size: 0.95rem;
            color: #333;
        }
        </style>
        <div class="chatassist-header">
            <h1>ChatAssist</h1>
            <p>Spinneys Lebanon support assistant. Ask about orders, delivery,
            payments, the mobile app, loyalty, refunds, gift cards, and more.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    init_state()

    try:
        client = get_client()
    except Exception as e:
        st.error(str(e))
        st.stop()

    render_sidebar()

    pending_input = st.session_state.pop("_pending_input", None)
    typed_input = st.chat_input("Type your question...")
    user_input = typed_input or pending_input

    if not st.session_state.messages and not user_input:
        with st.chat_message("assistant"):
            st.markdown(
                f"Hi! I'm **{ASSISTANT_NAME}**, your Spinneys Lebanon "
                "support assistant. How can I help you today?"
            )
            cols = st.columns(2)
            for i, prompt in enumerate(SUGGESTED_PROMPTS):
                if cols[i % 2].button(prompt, key=f"sug_{i}",
                                       use_container_width=True):
                    st.session_state["_pending_input"] = prompt
                    st.rerun()

    render_history()

    if not user_input:
        return

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    maybe_summarize(client)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        reply = stream_assistant_reply(client, user_input, placeholder)

        audio_bytes = None
        if st.session_state.tts_enabled and reply.strip():
            with st.spinner("Generating voice..."):
                audio_bytes = synthesize_speech(
                    client, reply, st.session_state.voice
                )
            if audio_bytes:
                st.audio(audio_bytes, format="audio/mp3")

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply,
        "audio": audio_bytes,
    })


if __name__ == "__main__":
    main()
