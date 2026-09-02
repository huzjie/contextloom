"""交叉编码器重排（可选依赖 sentence-transformers）。"""

from __future__ import annotations

from contextloom.core.models import SearchResult
from contextloom.rerank.base import BaseReranker


class CrossEncoderReranker(BaseReranker):
    def __init__(self, model_name: str) -> None:
        try:
            from sentence_transformers import CrossEncoder
        except ImportError as exc:
            raise RuntimeError("交叉编码器需安装：pip install 'contextloom[embeddings]'") from exc
        self._model = CrossEncoder(model_name)

    async def rerank(self, query, results):
        if not results:
            return []
        import asyncio
        pairs = [(query, r.text) for r in results]
        scores = await asyncio.to_thread(self._model.predict, pairs)
        order = sorted(range(len(results)), key=lambda i: scores[i], reverse=True)
        return [results[i] for i in order]
