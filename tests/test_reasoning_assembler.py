"""上下文装配器测试。"""
from contextloom.core.models import SearchResult
from contextloom.reasoning.assembler import ContextAssembler


def test_build_prompt():
    a = ContextAssembler(context_window=10000)
    rs = [SearchResult(chunk_id="c", document_id="d", text="参考片段", score=1.0)]
    system, prompt = a.build_prompt("问题？", rs)
    assert "参考片段" in prompt
    assert "问题" in prompt
    assert system


def test_dedup():
    a = ContextAssembler(context_window=10000)
    rs = [SearchResult(chunk_id="c", document_id="d", text="重复", score=1.0),
          SearchResult(chunk_id="c2", document_id="d", text="重复", score=0.9)]
    _, prompt = a.build_prompt("q", rs)
    assert prompt.count("重复") == 1
