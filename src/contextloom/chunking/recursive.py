"""递归字符分块器。"""

from __future__ import annotations

import re

from contextloom.chunking.base import BaseChunker

_SEPARATORS = ["\n\n", "\n", "。", "！", "？", ". ", "! ", "? ", "; ", "；", " "]


class RecursiveChunker(BaseChunker):
    def split(self, text: str, **kwargs) -> list[str]:
        if not text.strip():
            return []
        return _split_recursive(text, self.chunk_size, self.overlap, _SEPARATORS)


def _split_recursive(text: str, size: int, overlap: int, seps: list[str]) -> list[str]:
    if len(text) <= size:
        return [text]
    sep = next((s for s in seps if s in text), None)
    if sep is None:
        step = max(1, size - overlap)
        return [text[i:i + size] for i in range(0, len(text), step)]
    parts = re.split(f"({re.escape(sep)})", text)
    chunks: list[str] = []
    buf = ""
    for part in parts:
        if len(buf) + len(part) <= size:
            buf += part
        else:
            if buf.strip():
                chunks.append(buf)
            buf = part
            while len(buf) > size:
                chunks.append(buf[:size])
                buf = buf[size - overlap:]
    if buf.strip():
        chunks.append(buf)
    return chunks
