"""代码感知分块器。"""

from __future__ import annotations

import re

from contextloom.chunking.base import BaseChunker

_TOP = re.compile(
    r"^(def |class |async def |# |//|/\*|\*|pub fn |func |type |interface |export )",
    re.MULTILINE,
)


class CodeChunker(BaseChunker):
    def split(self, text: str, **kwargs) -> list[str]:
        if not text.strip():
            return []
        lines = text.splitlines(keepends=True)
        chunks: list[str] = []
        buf = ""
        for line in lines:
            if _TOP.match(line) and buf.strip():
                chunks.append(buf)
                buf = line
            else:
                buf += line
        if buf.strip():
            chunks.append(buf)
        return chunks
