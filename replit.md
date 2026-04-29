# Workspace

## Overview

pnpm workspace monorepo using TypeScript. Each package manages its own dependencies.

## Stack

- **Monorepo tool**: pnpm workspaces
- **Node.js version**: 24
- **Package manager**: pnpm
- **TypeScript version**: 5.9
- **API framework**: Express 5
- **Database**: PostgreSQL + Drizzle ORM
- **Validation**: Zod (`zod/v4`), `drizzle-zod`
- **API codegen**: Orval (from OpenAPI spec)
- **Build**: esbuild (CJS bundle)

## Key Commands

- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- `pnpm --filter @workspace/api-server run dev` — run API server locally

See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details.

## Python Chatbot

Standalone Python app at `chatbot/`:

- `chatbot/app.py` — Streamlit chatbot named **ChatAssist**, the Spinneys Lebanon support assistant
- `chatbot/knowledge.py` — knowledge base (topic links + FAQ Q&A) and keyword retriever
- `chatbot/.streamlit/config.toml` — Streamlit server config (port 5000)
- Workflow: `Chatbot` runs `cd chatbot && streamlit run app.py --server.port 5000`
- Uses Replit AI Integrations (OpenAI). Chat: `gpt-5.4`. Summarizer: `gpt-5-mini`. TTS via `gpt-audio-mini` chat completion with audio modality.
- Retrieval: each turn pulls the top ~5 keyword-matching FAQs into the system prompt (not the entire KB).
- Memory: when the recent buffer exceeds ~1500 tokens, older turns are condensed into a running summary by the cheap model and dropped from the buffer.
