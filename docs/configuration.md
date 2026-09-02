# 配置参考

所有配置通过环境变量（前缀 `CLOOM_`）或 `.env` 文件注入，由 pydantic-settings 解析。

| 变量 | 默认 | 说明 |
|------|------|------|
| CLOOM_LLM_BACKEND | ollama | ollama/llamacpp/vllm/sglang/openai/mock |
| CLOOM_LLM_MODEL | qwen3:8b | 模型名 |
| CLOOM_LLM_BASE_URL | http://localhost:11434 | 后端地址 |
| CLOOM_LLM_CONTEXT_WINDOW | 131072 | 上下文窗口，百万模型可调 1000000 |
| CLOOM_VECTOR_BACKEND | sqlite | sqlite/faiss/memory |
| CLOOM_CHUNK_SIZE | 1024 | 分块大小 |
| CLOOM_TOP_K | 8 | 检索条数 |

完整字段见 `src/contextloom/config/settings.py`。
