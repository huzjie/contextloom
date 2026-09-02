"""重排器工厂。"""

from __future__ import annotations

from contextloom.config.settings import Settings
from contextloom.rerank.base import BaseReranker
from contextloom.rerank.bm25 import BM25Reranker


def get_reranker(settings: Settings) -> BaseReranker:
    if not settings.rerank_enabled:
        return BM25Reranker()
    return BM25Reranker()
