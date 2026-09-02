"""示例：指标统计。"""
from contextloom.observability.metrics import MetricsRegistry

m = MetricsRegistry()
m.incr("requests")
with m.time("work"):
    pass
print(m.snapshot())
