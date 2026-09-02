"""FAISS 向量后端（可选依赖）。"""

from __future__ import annotations

from contextloom.core.models import Chunk, SearchResult
from contextloom.vectorstore.base import BaseVectorStore


class FaissStore(BaseVectorStore):
    name = "faiss"

    def __init__(self, dim: int = 512) -> None:
        try:
            import faiss  # type: ignore
        except ImportError as exc:
            raise RuntimeError("使用 FAISS 需安装：pip install 'contextloom[faiss]'") from exc
        self._faiss = faiss
        self._dim = dim
        self._index = faiss.IndexFlatIP(dim)
        self._chunks: list[Chunk] = []
        self._collections: dict[str, list[int]] = {}

    async def add(self, chunks: list[Chunk], collection: str) -> int:
        import numpy as np

        idx = self._collections.setdefault(collection, [])
        for c in chunks:
            if c.embedding is not None:
                vec = np.asarray(c.embedding, dtype=np.float32).reshape(1, -1)
                self._index.add(vec)
                self._chunks.append(c)
                idx.append(len(self._chunks) - 1)
        return len(chunks)

    async def search(self, query_embedding, query_text, collection, top_k):
        import numpy as np

        if not self._chunks:
            return []
        qvec = np.asarray(query_embedding, dtype=np.float32).reshape(1, -1)
        scores, indices = self._index.search(qvec, min(top_k, len(self._chunks)))
        results = []
        for s, i in zip(scores[0], indices[0]):
            if i < 0:
                continue
            c = self._chunks[int(i)]
            if c.collection != collection:
                continue
            results.append(SearchResult(chunk_id=c.id, document_id=c.document_id, text=c.text,
                                        score=float(s), heading=c.heading, metadata=c.metadata))
        return results

    async def delete_collection(self, collection: str) -> int:
        return len(self._collections.pop(collection, []))

    async def count(self, collection: str) -> int:
        return len(self._collections.get(collection, []))
