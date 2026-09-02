"""内存向量后端。"""

from __future__ import annotations

import math

from contextloom.core.models import Chunk, SearchResult
from contextloom.vectorstore.base import BaseVectorStore


class MemoryStore(BaseVectorStore):
    name = "memory"

    def __init__(self) -> None:
        self._chunks: dict[str, list[Chunk]] = {}

    async def add(self, chunks: list[Chunk], collection: str) -> int:
        self._chunks.setdefault(collection, []).extend(chunks)
        return len(chunks)

    async def search(self, query_embedding, query_text, collection, top_k):
        scored = []
        for c in self._chunks.get(collection, []):
            s = _cosine(query_embedding, c.embedding) if c.embedding else 0.0
            scored.append((s, c))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [SearchResult(chunk_id=c.id, document_id=c.document_id, text=c.text,
                             score=s, heading=c.heading, metadata=c.metadata)
                for s, c in scored[:top_k]]

    async def delete_collection(self, collection: str) -> int:
        return len(self._chunks.pop(collection, []))

    async def count(self, collection: str) -> int:
        return len(self._chunks.get(collection, []))


def _cosine(a: list[float], b: list[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)
