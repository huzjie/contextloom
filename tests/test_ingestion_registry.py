"""解析器注册表测试。"""
from contextloom.ingestion.registry import get_parser, supported_extensions


def test_supported():
    exts = supported_extensions()
    assert ".txt" in exts
    assert ".md" in exts
    assert ".pdf" in exts


def test_get_parser_by_ext():
    assert get_parser(".txt") is not None
    assert get_parser(".xyz") is None


def test_get_parser_by_path():
    assert get_parser("/tmp/a.md") is not None
