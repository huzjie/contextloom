"""滑动窗口分块器。"""

from __future__ import annotations

from contextloom.chunking.base import BaseChunker


class SlidingChunker(BaseChunker):
    def split(self, text: str, **kwargs) -> list[str]:
        if not text.strip():
            return []
        step = max(1, self.chunk_size - self.overlap)
        return [text[i:i + self.chunk_size] for i in range(0, len(text), step)]
