"""文档摄入与索引服务。"""

from __future__ import annotations

from contextloom.chunking.factory import get_chunker
from contextloom.core.models import Document
from contextloom.ingestion.ingestor import ingest_source
from contextloom.logging import get_logger
from contextloom.services.base import BaseService

logger = get_logger(__name__)


class DocumentService(BaseService):
    async def ingest(self, source: str, collection: str) -> dict:
        doc: Document = await ingest_source(source, collection)
        logger.info("解析完成: %s（%s）", doc.display_name, doc.format)

        chunker = get_chunker(self.settings.chunk_strategy,
                              chunk_size=self.settings.chunk_size,
                              overlap=self.settings.chunk_overlap)
        chunks = chunker.make_chunks(doc.source or "", doc.id, collection, heading=doc.title)

        # 从解析结果拿正文（ingestor 已存 source 字段，这里重新取解析文本）
        from contextloom.ingestion.ingestor import ingest_source as _is
        # 兼容：重新解析以取得正文
        chunks = await self._build_chunks(source, collection, doc, chunker)

        vectors = await self.embedder.embed([c.text for c in chunks]) if chunks else []
        for c, vec in zip(chunks, vectors):
            c.embedding = vec
        count = await self.store.add(chunks, collection)
        logger.info("已写入 %d 个分块到知识库 %s", count, collection)
        return {"document_id": doc.id, "title": doc.display_name,
                "chunks": count, "collection": collection}

    async def _build_chunks(self, source, collection, doc, chunker):
        from contextloom.ingestion.base import ParsedDocument

        if source.startswith("http"):
            from contextloom.ingestion.registry import get_parser
            parser = get_parser(".url")
            parsed = await parser.parse(source) if parser else ParsedDocument()
        else:
            from pathlib import Path
            from contextloom.ingestion.registry import get_parser
            p = Path(source)
            parser = get_parser(".repo") if p.is_dir() else get_parser(p.suffix)
            parsed = await parser.parse(p) if parser else ParsedDocument()
        return chunker.make_chunks(parsed.text, doc.id, collection, heading=doc.title)
