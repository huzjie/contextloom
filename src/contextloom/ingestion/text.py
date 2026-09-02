"""纯文本解析器。"""

from __future__ import annotations

from pathlib import Path

from contextloom.ingestion.base import BaseParser, ParsedDocument
from contextloom.ingestion.registry import register_parser


@register_parser(".txt", ".text", ".log", ".csv", ".json", ".yaml", ".yml")
class TextParser(BaseParser):
    extensions = (".txt", ".text", ".log", ".csv", ".json", ".yaml", ".yml")

    async def parse(self, path: str | Path) -> ParsedDocument:
        p = Path(path)
        text = self._read_text(p)
        return ParsedDocument(title=p.stem, text=text, source=str(p),
                              metadata={"format": "text", "size": p.stat().st_size})
