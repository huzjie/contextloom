# 本地大模型后端接入

## Ollama

```bash
ollama pull qwen3:8b
CLOOM_LLM_BACKEND=ollama CLOOM_LLM_BASE_URL=http://localhost:11434
```

## llama.cpp server

```bash
llama-server -m model.gguf --port 8080
CLOOM_LLM_BACKEND=llamacpp CLOOM_LLM_BASE_URL=http://localhost:8080
```

## vLLM / SGLang

两者均暴露 OpenAI 兼容 `/v1/chat/completions`，按 openai 协议接入。

## 星火 X2.5 端侧模型

词元星火开源星火 X2.5-4B/1.7B 支持 vLLM / SGLang / llama.cpp，将 `CLOOM_LLM_CONTEXT_WINDOW`
调至 1000000，即可让模型一次性读完百万 token 长文档。
