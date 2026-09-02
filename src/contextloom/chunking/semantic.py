"""语义分块器（句子边界）。"""

from __future__ import annotations

import re

from contextloom.chunking.base import BaseChunker

_SENTENCE = re.compile(r"(?<=[。！？.!?])\s*")


class SemanticChunker(BaseChunker):
    def split(self, text: str, **kwargs) -> list[str]:
        if not text.strip():
            return []
        sentences = [s.strip() for s in _SENTENCE.split(text) if s.strip()]
        chunks: list[str] = []
        buf = ""
        for sent in sentences:
            if len(buf) + len(sent) <= self.chunk_size:
                buf += sent
            else:
                if buf:
                    chunks.append(buf)
                buf = sent
        if buf:
            chunks.append(buf)
        return chunks
