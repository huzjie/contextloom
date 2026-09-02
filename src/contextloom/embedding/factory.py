"""向量化器工厂。"""

from __future__ import annotations

from contextloom.config.settings import Settings
from contextloom.embedding.base import BaseEmbedder
from contextloom.embedding.hash_embedder import HashEmbedder
from contextloom.logging import get_logger

logger = get_logger(__name__)


class _SentAdapter(BaseEmbedder):
    def __init__(self, model: str) -> None:
        from contextloom.embedding.sentence_embedder import SentenceEmbedder
        self._inner = SentenceEmbedder(model)

    async def embed(self, texts: list[str]) -> list[list[float]]:
        return await self._inner.embed(texts)


def get_embedder(settings: Settings) -> BaseEmbedder:
    try:
        return _SentAdapter(settings.embed_model)
    except Exception as exc:
        if settings.embed_allow_hash_fallback:
            logger.warning("真实 embedding 不可用（%s），降级为哈希向量化", exc)
            return HashEmbedder(dim=settings.embed_dim)
        raise
