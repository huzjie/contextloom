"""Markdown 解析器测试。"""
import pytest

from contextloom.ingestion.markdown import MarkdownParser


@pytest.mark.asyncio
async def test_parse(tmp_path):
    p = tmp_path / "a.md"
    p.write_text("# 标题\n正文内容", encoding="utf-8")
    doc = await MarkdownParser().parse(p)
    assert doc.title == "标题"
    assert "标题" in doc.headings
