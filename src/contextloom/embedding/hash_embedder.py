"""哈希降级向量化（无真实模型时兜底）。"""

from __future__ import annotations

import hashlib
import math
import re


class HashEmbedder:
    def __init__(self, dim: int = 512, n: int = 3) -> None:
        self.dim = dim
        self.n = n

    async def embed(self, texts: list[str]) -> list[list[float]]:
        return [self._embed_one(t) for t in texts]

    def _embed_one(self, text: str) -> list[float]:
        vec = [0.0] * self.dim
        for g in _ngrams(text, self.n):
            h = int(hashlib.md5(g.encode("utf-8")).hexdigest(), 16)
            idx = h % self.dim
            sign = 1.0 if (h >> 8) % 2 == 0 else -1.0
            vec[idx] += sign
        norm = math.sqrt(sum(v * v for v in vec)) or 1.0
        return [v / norm for v in vec]


def _ngrams(text: str, n: int) -> list[str]:
    cleaned = re.sub(r"\s+", "", text)
    if len(cleaned) <= n:
        return [cleaned] if cleaned else []
    return [cleaned[i:i + n] for i in range(len(cleaned) - n + 1)]
