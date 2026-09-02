"""分块器基类。"""

from __future__ import annotations

from abc import ABC, abstractmethod
import re

from contextloom.core.models import Chunk


class BaseChunker(ABC):
    def __init__(self, chunk_size: int = 1024, overlap: int = 128) -> None:
        self.chunk_size = chunk_size
        self.overlap = overlap

    @abstractmethod
    def split(self, text: str, **kwargs) -> list[str]:
        ...

    def make_chunks(self, text: str, document_id: str, collection: str,
                    heading: str = "", metadata: dict | None = None) -> list[Chunk]:
        from contextloom.core.ids import chunk_id

        pieces = self.split(text)
        chunks: list[Chunk] = []
        for i, piece in enumerate(pieces):
            piece = piece.strip()
            if not piece:
                continue
            chunks.append(Chunk(
                id=chunk_id(document_id, i),
                document_id=document_id,
                collection=collection,
                text=piece,
                index=i,
                heading=heading,
                token_count=_approx_tokens(piece),
                metadata=metadata or {},
            ))
        return chunks


def _approx_tokens(text: str) -> int:
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    other = len(text) - cjk
    return cjk + max(1, other // 4)
