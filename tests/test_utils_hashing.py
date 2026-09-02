"""哈希工具测试。"""
from contextloom.utils.hashing import md5, sha256, short_hash


def test_md5():
    assert len(md5("x")) == 32


def test_short():
    assert len(short_hash("abc", 8)) == 8
