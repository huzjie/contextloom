"""带 TTL 的线程安全缓存。"""

from __future__ import annotations

import threading
import time
from typing import Any, Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class TTLCache(Generic[K, V]):
    def __init__(self, ttl_seconds: float = 60.0, maxsize: int = 1000) -> None:
        self.ttl = ttl_seconds
        self.maxsize = maxsize
        self._data: dict[K, tuple[float, V]] = {}
        self._lock = threading.Lock()

    def get(self, key: K) -> V | None:
        with self._lock:
            item = self._data.get(key)
            if item is None:
                return None
            ts, val = item
            if time.monotonic() - ts > self.ttl:
                self._data.pop(key, None)
                return None
            return val

    def set(self, key: K, value: V) -> None:
        with self._lock:
            if len(self._data) >= self.maxsize:
                oldest = min(self._data, key=lambda k: self._data[k][0])
                self._data.pop(oldest, None)
            self._data[key] = (time.monotonic(), value)

    def clear(self) -> None:
        with self._lock:
            self._data.clear()
