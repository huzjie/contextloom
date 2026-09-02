"""文档服务测试。"""
import pytest

from contextloom.config.settings import Settings
from contextloom.services.document_service import DocumentService


@pytest.mark.asyncio
async def test_ingest(settings, tmp_path):
    p = tmp_path / "a.md"
    p.write_text("# 标题\n这是正文内容。", encoding="utf-8")
    svc = DocumentService(settings)
    r = await svc.ingest(str(p), "col")
    assert r["chunks"] >= 1
    assert r["collection"] == "col"
