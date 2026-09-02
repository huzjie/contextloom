"""重排器基类。"""

from __future__ import annotations

from abc import ABC, abstractmethod

from contextloom.core.models import SearchResult


class BaseReranker(ABC):
    @abstractmethod
    async def rerank(self, query: str, results: list[SearchResult]) -> list[SearchResult]:
        ...
