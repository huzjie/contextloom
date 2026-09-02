# ContextLoom 项目详细介绍

> 这是一份「怎么用 + 怎么实现」的完整说明，写给想要快速上手、二次开发的你。

## 一句话定位

**ContextLoom 是一个端侧（本地/离线）的百万 Token 长文档智能平台**——把几十页手册、
整份代码仓库、一堆会议材料一次性交给本地大模型，跨章节读懂并完成任务，数据不出本机。

## 它解决什么问题

本地大模型（尤其星火 X2.5-4B/1.7B 这类支持百万上下文的端侧模型）已经具备「一次性读完
整份文档」的能力，但缺一套工程把它变成能用的工具：

1. **文档怎么进？** PDF/DOCX/Markdown/HTML/代码目录/URL 全都要能解析。
2. **长文档怎么切？** 既要切得语义完整，又要能精确检索。
3. **怎么检索？** 关键词 + 语义向量混合，快且准。
4. **怎么喂给模型？** 百万上下文也要省着用，token 预算要管好。
5. **怎么跨章节推理？** 把散落的规则织成完整上下文再让模型综合判断。
6. **怎么落地？** 要有 CLI、REST API、Web 控制台、Docker/K8s。

ContextLoom 就是这六个问题的完整答案。

## 核心模块清单

| 模块 | 文件数 | 说明 |
|------|--------|------|
| 摄入 `ingestion/` | 10 | 8 种格式解析器 + 注册表 + 编排器 |
| 分块 `chunking/` | 6 | 4 种策略 + 工厂 |
| 向量 `vectorstore/` | 6 | SQLite-FTS / FAISS / 内存 |
| 向量化 `embedding/` | 5 | 真实模型 + 哈希降级 |
| 大模型 `llm/` | 9 | Ollama/llama.cpp/vLLM/SGLang/OpenAI/Mock |
| 推理 `reasoning/` | 3 | 上下文装配 + 推理引擎 |
| 服务 `services/` | 4 | 文档/问答编排 |
| 接口 `api/` `cli/` `webui/` | 16 | REST + CLI + Web |
| 工具 `utils/` `workers/` | 6 | token 估算、哈希、任务队列 |

## 三种使用方式

### 1. 命令行（最快）

```bash
contextloom ingest docs/demo/售后手册.md --collection support
contextloom ask "购买 10 天后故障能否换货" --collection support
```

### 2. REST API（自动化）

```bash
contextloom serve
curl -X POST localhost:8000/queries/ask \
  -H 'Content-Type: application/json' \
  -d '{"question":"...","collection":"support"}'
```

### 3. Web 控制台（可视化）

启动服务后打开 `http://localhost:8000/ui`。

## 技术亮点

- **零强依赖**：核心只依赖标准库 + fastapi/pydantic/numpy，可选能力（PDF/DOCX/FAISS/真实 embedding）全部惰性导入。
- **工厂 + 注册表**：新增解析器/后端只需一个装饰器或一行注册，不改主流程。
- **端侧优先**：默认连本地 Ollama，全程离线；也兼容任意 OpenAI 兼容端点。
- **生产就绪**：健康检查、后台任务队列、CI/CD、Docker/K8s、完整测试套件。

## 目录结构（完整）

见 `docs/architecture.md` 与仓库根目录 `tree`。

## 如何开始贡献

见 `CONTRIBUTING.md`。
