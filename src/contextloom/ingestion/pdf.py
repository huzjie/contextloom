"""PDF 解析器（可选依赖 pypdf）。"""

from __future__ import annotations

from pathlib import Path

from contextloom.ingestion.base import BaseParser, ParsedDocument
from contextloom.ingestion.registry import register_parser


@register_parser(".pdf")
class PdfParser(BaseParser):
    extensions = (".pdf",)

    async def parse(self, path: str | Path) -> ParsedDocument:
        p = Path(path)
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise RuntimeError("解析 PDF 需要安装：pip install 'contextloom[pdf]'") from exc
        reader = PdfReader(str(p))
        text = "\n\n".join(page.extract_text() or "" for page in reader.pages)
        meta = reader.metadata or {}
        return ParsedDocument(title=str(meta.title or p.stem), text=text, source=str(p),
                              metadata={"format": "pdf", "pages": len(reader.pages)})
