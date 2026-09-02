"""HTML 解析器（标准库降级实现）。"""

from __future__ import annotations

import re
from html import unescape
from pathlib import Path

from contextloom.ingestion.base import BaseParser, ParsedDocument
from contextloom.ingestion.registry import register_parser

_TAG = re.compile(r"<[^>]+>")
_SCRIPT = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.DOTALL | re.IGNORECASE)


@register_parser(".html", ".htm", ".xhtml")
class HtmlParser(BaseParser):
    extensions = (".html", ".htm", ".xhtml")

    async def parse(self, path: str | Path) -> ParsedDocument:
        p = Path(path)
        raw = _SCRIPT.sub(" ", self._read_text(p))
        tm = re.search(r"<title[^>]*>(.*?)</title>", raw, re.IGNORECASE | re.DOTALL)
        title = unescape(tm.group(1)).strip() if tm else p.stem
        text = _TAG.sub(" ", raw)
        text = unescape(text)
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        text = re.sub(r"\n\s*\n+", "\n\n", text)
        return ParsedDocument(title=title, text=text.strip(), source=str(p),
                              metadata={"format": "html"})
