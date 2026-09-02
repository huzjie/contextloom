"""向量存储基类。"""

from __future__ import annotations

from abc import ABC, abstractmethod

from contextloom.core.models import Chunk, SearchResult


class BaseVectorStore(ABC):
    name = "base"

    @abstractmethod
    async def add(self, chunks: list[Chunk], collection: str) -> int:
        ...

    @abstractmethod
    async def search(self, query_embedding: list[float], query_text: str,
                     collection: str, top_k: int) -> list[SearchResult]:
        ...

    @abstractmethod
    async def delete_collection(self, collection: str) -> int:
        ...

    @abstractmethod
    async def count(self, collection: str) -> int:
        ...
