"""URL 网页摄入器。"""

from __future__ import annotations

import re
from html import unescape

import httpx

from contextloom.ingestion.base import BaseParser, ParsedDocument
from contextloom.ingestion.registry import register_parser

_TAG = re.compile(r"<[^>]+>")
_SCRIPT = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.DOTALL | re.IGNORECASE)


@register_parser(".url")
class UrlParser(BaseParser):
    extensions = (".url",)

    async def parse(self, path: str | Path) -> ParsedDocument:
        url = str(path)
        async with httpx.AsyncClient(follow_redirects=True, timeout=30) as client:
            resp = await client.get(url)
            resp.raise_for_status()
            raw = _SCRIPT.sub(" ", resp.text)
        tm = re.search(r"<title[^>]*>(.*?)</title>", raw, re.IGNORECASE | re.DOTALL)
        title = unescape(tm.group(1)).strip() if tm else url
        text = unescape(_TAG.sub(" ", raw))
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        return ParsedDocument(title=title, text=text.strip(), source=url,
                              metadata={"format": "url"})
