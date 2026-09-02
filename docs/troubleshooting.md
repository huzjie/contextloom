# 故障排查

- **连接 Ollama 失败**：确认 `ollama serve` 已启动，端口 11434。
- **解析 PDF 报错**：`pip install 'contextloom[pdf]'`。
- **向量维度不匹配**：检查 `CLOOM_EMBED_DIM` 与模型输出维度一致。
