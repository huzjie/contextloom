"""领域模型测试。"""
from contextloom.core.models import Chunk, Document, SearchResult


def test_document_display_name():
    d = Document(id="1", collection="c", title="标题")
    assert d.display_name == "标题"


def test_chunk_defaults():
    c = Chunk(id="x", document_id="d", collection="c", text="hello")
    assert c.embedding is None
    assert c.index == 0


def test_search_result():
    r = SearchResult(chunk_id="c", document_id="d", text="t", score=0.9)
    assert r.score > 0
