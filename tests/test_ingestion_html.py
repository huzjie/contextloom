"""HTML 解析器测试。"""
import pytest

from contextloom.ingestion.html import HtmlParser


@pytest.mark.asyncio
async def test_parse(tmp_path):
    p = tmp_path / "a.html"
    p.write_text("<html><head><title>页标题</title></head><body><p>正文</p></body></html>",
                 encoding="utf-8")
    doc = await HtmlParser().parse(p)
    assert doc.title == "页标题"
    assert "正文" in doc.text
