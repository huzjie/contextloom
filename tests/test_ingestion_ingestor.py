"""摄入编排器测试。"""
import pytest

from contextloom.ingestion.ingestor import ingest_source


@pytest.mark.asyncio
async def test_ingest_md(tmp_path):
    p = tmp_path / "a.md"
    p.write_text("# T\n正文", encoding="utf-8")
    doc = await ingest_source(str(p), "coll")
    assert doc.collection == "coll"
    assert doc.title == "T"
