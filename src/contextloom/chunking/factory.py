"""分块器工厂。"""

from __future__ import annotations

from contextloom.chunking.base import BaseChunker
from contextloom.chunking.code import CodeChunker
from contextloom.chunking.recursive import RecursiveChunker
from contextloom.chunking.semantic import SemanticChunker
from contextloom.chunking.sliding import SlidingChunker

_STRATEGIES: dict[str, type[BaseChunker]] = {
    "recursive": RecursiveChunker,
    "semantic": SemanticChunker,
    "code": CodeChunker,
    "sliding": SlidingChunker,
}


def get_chunker(strategy: str, chunk_size: int = 1024, overlap: int = 128) -> BaseChunker:
    cls = _STRATEGIES.get(strategy)
    if cls is None:
        raise ValueError(f"未知分块策略: {strategy}，可选: {list(_STRATEGIES)}")
    return cls(chunk_size=chunk_size, overlap=overlap)
