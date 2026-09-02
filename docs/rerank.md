# 重排器

检索出 top_k 后，可用重排器进一步精排。当前内置 BM25 与交叉编码器。

```python
from contextloom.rerank.factory import get_reranker
reranker = get_reranker(settings)
results = await reranker.rerank(query, results)
```
