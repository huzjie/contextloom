"""BM25 关键词重排器（零依赖）。"""

from __future__ import annotations

import math
import re

from contextloom.core.models import SearchResult
from contextloom.rerank.base import BaseReranker

_TOKEN = re.compile(r"[\u4e00-\u9fff]|[a-zA-Z0-9]+")


class BM25Reranker(BaseReranker):
    def __init__(self, k1: float = 1.5, b: float = 0.75) -> None:
        self.k1 = k1
        self.b = b

    async def rerank(self, query, results):
        if not results:
            return []
        docs = [r.text for r in results]
        q_terms = _tokenize(query)
        N = len(docs)
        avgdl = sum(len(d) for d in docs) / max(1, N)
        scores = []
        for r, d in zip(results, docs):
            tf = {t: d.count(t) for t in set(_tokenize(d))}
            dl = len(d)
            score = 0.0
            for t in q_terms:
                f = tf.get(t, 0)
                if f == 0:
                    continue
                df = sum(1 for x in docs if t in x)
                idf = math.log(1 + (N - df + 0.5) / (df + 0.5))
                score += idf * (f * (self.k1 + 1)) / (f + self.k1 * (1 - self.b + self.b * dl / avgdl))
            scores.append(score)
        order = sorted(range(len(results)), key=lambda i: scores[i], reverse=True)
        return [results[i] for i in order]


def _tokenize(text: str) -> list[str]:
    return [m.group(0).lower() for m in _TOKEN.finditer(text)]
