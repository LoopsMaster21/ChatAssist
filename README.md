# ChatAssist — Spinneys Lebanon Virtual Assistant

ChatAssist is a Streamlit-based AI chatbot that answers customer questions about Spinneys Lebanon (spinneyslebanon.com): accounts, orders, delivery, payments, the mobile app, loyalty rewards, gift cards, refunds, and contact info.

It is grounded in a curated FAQ knowledge base, supports voice replies (TTS), and uses a token-efficient memory strategy so long conversations stay cheap.

---

## Features

- **Spinneys-only answers.** The assistant only replies using the built-in knowledge base. If a question is not covered, it points the customer to the Call Center (1521) or the Contact Us page.
- **Welcome buttons.** New users see quick-start buttons for common topics (Orders, Delivery, Payments, etc.). Buttons disappear as soon as the conversation starts.
- **Voice replies (TTS).** Each assistant message can be played back as audio. The user picks a voice (alloy, echo, fable, onyx, nova, shimmer) from the sidebar.
- **Token-optimized memory.** After every turn, older messages are condensed into a running summary by a cheaper model and dropped from the live buffer. Only the last couple of messages plus the summary are sent on each request.
- **Knowledge retrieval.** Each turn pulls only the top ~5 keyword-matching FAQ entries into the system prompt, instead of stuffing the whole knowledge base.
- **Spinneys-yellow branded header.** Custom CSS banner using the Spinneys yellow (#FFD200).

---

## Project structure

```
artifacts/chatbot/
├── app.py                        # Streamlit app: UI, chat loop, memory, TTS
├── knowledge.py                  # FAQ knowledge base + keyword retriever
├── .streamlit/
│   └── config.toml               # Streamlit server settings (port 5000, headless)
└── .replit-artifact/
    └── artifact.toml             # Artifact + deployment configuration
```

---

## How it works

### 1. Conversation flow
1. User sends a message (or clicks a welcome button).
2. The retriever scans the FAQ knowledge base and returns the top matching entries.
3. Those entries are injected into the system prompt as fresh context.
4. The chat model receives: system prompt + running summary + last couple of messages + new user message.
5. The reply is streamed back into the UI.
6. After the turn, older messages are summarized and removed from the live buffer.

### 2. Memory strategy
- `KEEP_RECENT_MESSAGES = 2` — only the last two messages stay in the live buffer.
- Everything older is rolled into a single running summary by a small/cheap model.
- This keeps every request small regardless of conversation length.

### 3. Models
| Purpose      | Model            |
|--------------|------------------|
| Chat replies | `gpt-5.4`        |
| Summarizer   | `gpt-5-mini`     |
| Voice (TTS)  | `gpt-audio-mini` |

All models are accessed through Replit AI Integrations — **no user API key required**.

---

## Knowledge base

`knowledge.py` contains:
- `TOPIC_INDEX` — the high-level list of store sections used in the system prompt.
- A list of FAQ entries (question + answer + tags).
- `retrieve_relevant(query)` — keyword-overlap retriever that returns the top entries.
- `format_context(entries)` — formats retrieved entries for injection into the prompt.

To extend ChatAssist's knowledge, add new entries to the FAQ list in `knowledge.py`.

---

## Configuration

- **Port:** `5000` (set in `.streamlit/config.toml` and `artifact.toml`)
- **Address:** `0.0.0.0`, headless mode on
- **Default voice:** `nova` (changeable in the sidebar)

---

## Running locally on Replit

The app runs as a workflow:

```
streamlit run app.py --server.port 5000
```

Restart the `artifacts/chatbot: Chatbot` workflow after any code change.

---

## Deployment

ChatAssist is configured as a deployable artifact. Production run command (from `artifact.toml`):

```
streamlit run artifacts/chatbot/app.py \
  --server.port 5000 \
  --server.address 0.0.0.0 \
  --server.headless true \
  --server.enableCORS false \
  --server.enableXsrfProtection false
```

Health check path: `/_stcore/health`.

Use Replit's Publish button to deploy.

---

## Usage tips

- Pick a voice in the sidebar before sending a message if you want audio replies.
- The "Reset chat" button clears the conversation and the running summary.
- If the assistant doesn't know an answer, it will direct customers to **Call Center 1521** (10am–10pm, 7 days a week) or the [Contact Us page](https://www.spinneyslebanon.com/default/contact/).
