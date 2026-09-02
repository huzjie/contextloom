"""LLM 基类测试。"""
import pytest

from contextloom.llm.mock import MockBackend


@pytest.mark.asyncio
async def test_stream_fallback():
    b = MockBackend("http://x/", "m")
    out = [x async for x in b.stream("hi")]
    assert out
