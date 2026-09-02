"""示例：使用 TTL 缓存。"""
from contextloom.cache.ttl import TTLCache

c = TTLCache[str, str](ttl_seconds=30)
c.set("greeting", "hello")
print(c.get("greeting"))
