# Changelog

本项目遵循 Semantic Versioning，格式遵循 Keep a Changelog。

## [0.1.0] - 2026-09-02

### Added

- 初始版本：端侧百万上下文文档智能平台。
- 多格式文档摄入（PDF/DOCX/Markdown/HTML/文本/代码/URL）。
- 四种分块策略（递归/语义/代码感知/滑动窗口）。
- 三种向量后端（SQLite-FTS + NumPy / FAISS / 内存）。
- 六种 LLM 后端（Ollama / llama.cpp / vLLM / SGLang / OpenAI 兼容 / Mock）。
- 跨章节推理引擎与上下文装配器。
- REST API、CLI、简易 Web 控制台。
- Docker / docker-compose / K8s 部署清单。
- CI/CD 与完整测试套件。
