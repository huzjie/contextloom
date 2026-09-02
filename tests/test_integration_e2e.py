"""端到端集成测试（mock + memory）。"""
import pytest

from contextloom.config.settings import Settings
from contextloom.services.document_service import DocumentService
from contextloom.services.query_service import QueryService


@pytest.mark.asyncio
async def test_e2e(tmp_path):
    s = Settings(llm_backend="mock", vector_backend="memory",
                 embed_allow_hash_fallback=True, data_dir=tmp_path, _env_file=None)
    p = tmp_path / "manual.md"
    p.write_text("# 售后手册\n购买后 10 天内可无理由退换。\n使用第三方耗材则不保修。",
                 encoding="utf-8")
    await DocumentService(s).ingest(str(p), "support")
    answer = await QueryService(s).ask("用第三方耗材还能退吗", "support")
    assert answer.answer
    assert answer.backend == "mock"
