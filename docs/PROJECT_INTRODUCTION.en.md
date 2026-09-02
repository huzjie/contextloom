# ContextLoom — Project Deep Dive

ContextLoom is an **on-device long-context document intelligence platform**. It ingests
large documents (manuals, code repos, meeting notes), indexes them, and answers
cross-chapter questions using a local LLM — fully offline.

## Why

On-device models with million-token context (e.g. Spark X2.5-4B) can read an entire
manual in one pass. ContextLoom provides the missing engineering: parsing, chunking,
hybrid retrieval, token-budgeted context assembly, cross-chapter reasoning, and
service/CLI/web surfaces.

## Modules

- `ingestion/` — 8 format parsers + registry
- `chunking/` — 4 strategies + factory
- `vectorstore/` — SQLite-FTS / FAISS / memory
- `llm/` — Ollama / llama.cpp / vLLM / SGLang / OpenAI-compatible / mock
- `reasoning/` — context assembler + engine
- `api/`, `cli/`, `webui/` — three interfaces

## Quick Start

```bash
pip install -e .
contextloom ingest manual.md --collection support
contextloom ask "Can I return this?" --collection support
```
