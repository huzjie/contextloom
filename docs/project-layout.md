# 项目目录完整说明

```
contextloom/
├── src/contextloom/
│   ├── api/          # FastAPI 路由 + 应用工厂 + 依赖注入
│   ├── cache/        # TTL 缓存 / 向量缓存
│   ├── chunking/     # 4 种分块策略
│   ├── cli/          # Typer 命令行
│   ├── config/       # pydantic-settings 配置
│   ├── core/         # 领域模型 + ID 生成
│   ├── embedding/    # 向量化 + 哈希降级
│   ├── ingestion/    # 8 种解析器 + 注册表
│   ├── llm/          # 6 种 LLM 后端
│   ├── observability/# 指标 + 追踪 + 中间件
│   ├── reasoning/    # 上下文装配 + 推理引擎
│   ├── rerank/       # 重排器
│   ├── security/     # 清理 + 脱敏
│   ├── services/     # 文档 / 问答编排
│   ├── utils/        # token 估算 / 哈希 / IO
│   ├── vectorstore/  # SQLite / FAISS / 内存
│   ├── webui/        # 静态 Web 控制台
│   └── workers/      # 后台任务队列
├── tests/            # 70+ 测试
├── docs/             # 20+ 文档
├── deploy/           # K8s / nginx / systemd
├── scripts/          # 基准 / 种子 / 健康检查
├── examples/         # 使用示例
└── .github/          # CI/CD / Issue 模板
```
