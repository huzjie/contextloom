"""Mock 后端测试。"""
import pytest

from contextloom.llm.mock import MockBackend


@pytest.mark.asyncio
async def test_complete():
    b = MockBackend("http://x", "m")
    r = await b.complete("问题内容")
    assert "mock" in r.text
    assert r.model == "m"
