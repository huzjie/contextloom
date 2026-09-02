# 性能优化

- 端侧小模型（4B/1.7B）CPU 即可推理，延迟主要受分块数与上下文长度影响。
- 使用 `CLOOM_CHUNK_SIZE` 调小分块可降低单次检索开销。
- 大数据量场景建议切 FAISS 后端。
- 向量化结果可用 `EmbeddingCache` 缓存。
