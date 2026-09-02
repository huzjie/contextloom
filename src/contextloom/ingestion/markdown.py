"""Markdown 解析器。"""

from __future__ import annotations

import re
from pathlib import Path

from contextloom.ingestion.base import BaseParser, ParsedDocument
from contextloom.ingestion.registry import register_parser

_HEADING = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)


@register_parser(".md", ".markdown", ".mdx")
class MarkdownParser(BaseParser):
    extensions = (".md", ".markdown", ".mdx")

    async def parse(self, path: str | Path) -> ParsedDocument:
        p = Path(path)
        text = self._read_text(p)
        headings = [m.group(2).strip() for m in _HEADING.finditer(text)]
        title = headings[0] if headings else p.stem
        return ParsedDocument(title=title, text=text, headings=headings,
                              source=str(p), metadata={"format": "markdown"})
