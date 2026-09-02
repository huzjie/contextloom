"""向量化结果缓存。"""

from __future__ import annotations

import hashlib

from contextloom.cache.ttl import TTLCache


class EmbeddingCache:
    def __init__(self, ttl_seconds: float = 300.0) -> None:
        self._cache: TTLCache[str, list[float]] = TTLCache(ttl_seconds)

    def get(self, text: str) -> list[float] | None:
        return self._cache.get(_key(text))

    def set(self, text: str, vec: list[float]) -> None:
        self._cache.set(_key(text), vec)


def _key(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()
