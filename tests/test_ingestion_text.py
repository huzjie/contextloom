"""文本解析器测试。"""
import pytest

from contextloom.ingestion.text import TextParser


@pytest.mark.asyncio
async def test_parse(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("hello world", encoding="utf-8")
    doc = await TextParser().parse(p)
    assert doc.text == "hello world"
    assert doc.title == "a"
