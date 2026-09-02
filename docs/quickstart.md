# 5 分钟上手

```bash
pip install -e .
cp .env.example .env          # 改成 mock 后端即可离线体验
contextloom ingest docs/demo/售后手册.md --collection support
contextloom ask "购买 10 天后设备故障能否换货" --collection support
contextloom serve              # 打开 http://localhost:8000/docs
```

使用真实本地模型：

```bash
ollama pull qwen3:8b
# 在 .env 中保持 CLOOM_LLM_BACKEND=ollama
contextloom ingest docs/demo/售后手册.md
contextloom ask "用第三方耗材还保修吗"
```
