"""推理引擎测试。"""
import pytest

from contextloom.config.settings import Settings
from contextloom.reasoning.engine import ReasoningEngine


@pytest.mark.asyncio
async def test_answer_mock(settings):
    engine = ReasoningEngine(settings)
    a = await engine.answer("测试问题", "col")
    assert a.answer
    assert a.backend == "mock"
    assert a.elapsed_ms >= 0
