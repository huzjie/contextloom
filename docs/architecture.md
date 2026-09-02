# 系统架构

## 分层

| 层 | 目录 | 职责 |
|----|------|------|
| 摄入层 | `ingestion/` | 解析 PDF/DOCX/MD/HTML/代码/URL |
| 分块层 | `chunking/` | 递归/语义/代码/滑动切分 |
| 索引层 | `vectorstore/` | SQLite-FTS / FAISS / 内存 |
| 向量层 | `embedding/` | 真实模型或哈希降级 |
| 推理层 | `reasoning/` | 检索 + 上下文装配 + LLM |
| 服务层 | `services/` | 文档 / 问答编排 |
| 接口层 | `api/` `cli/` `webui/` | REST / 命令行 / Web |

## 数据流

1. 用户提交来源（文件/目录/URL）。
2. 摄入层解析出结构化 `ParsedDocument`。
3. 分块层切成 `Chunk` 列表。
4. 向量层批量 embedding。
5. 索引层持久化（文本 + 向量）。
6. 提问时：问题向量化 → 检索 top_k → 上下文装配（token 预算）→ 本地 LLM 生成答案。

## 设计原则

- **插件化**：解析器 / 分块器 / 向量后端 / LLM 后端均通过注册表或工厂扩展。
- **零强依赖**：核心路径仅依赖标准库 + fastapi/pydantic/numpy，可选能力惰性导入。
- **端侧优先**：数据不出本机，模型走本地 Ollama/llama.cpp/vLLM。
