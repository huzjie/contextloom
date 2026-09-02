"""问答服务测试。"""
import pytest

from contextloom.config.settings import Settings
from contextloom.services.query_service import QueryService


@pytest.mark.asyncio
async def test_ask(settings):
    svc = QueryService(settings)
    a = await svc.ask("问题", "col")
    assert a.answer
