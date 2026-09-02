"""TTL 缓存测试。"""
import time

from contextloom.cache.ttl import TTLCache


def test_set_get():
    c = TTLCache[int, str](ttl_seconds=10)
    c.set(1, "a")
    assert c.get(1) == "a"
    assert c.get(2) is None


def test_expiry():
    c = TTLCache[int, str](ttl_seconds=0.05)
    c.set(1, "a")
    time.sleep(0.08)
    assert c.get(1) is None
