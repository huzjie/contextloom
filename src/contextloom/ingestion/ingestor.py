"""摄入编排器。"""

from __future__ import annotations

from pathlib import Path

from contextloom.core.ids import doc_id
from contextloom.core.models import Document
from contextloom.ingestion.base import ParsedDocument
from contextloom.ingestion.registry import get_parser, supported_extensions
from contextloom.logging import get_logger

logger = get_logger(__name__)


async def ingest_source(source: str, collection: str) -> Document:
    if source.startswith("http://") or source.startswith("https://"):
        parser = get_parser(".url")
        parsed = await parser.parse(source) if parser else None
    else:
        p = Path(source)
        parser = get_parser(".repo") if p.is_dir() else get_parser(p.suffix)
        if parser is None:
            raise ValueError(f"不支持的文件格式: {p.suffix}，支持: {supported_extensions()}")
        parsed = await parser.parse(p)

    assert isinstance(parsed, ParsedDocument)
    return Document(
        id=doc_id(source),
        collection=collection,
        title=parsed.title,
        source=source,
        path=source,
        format=str(parsed.metadata.get("format", "text")),
        metadata=parsed.metadata,
    )
