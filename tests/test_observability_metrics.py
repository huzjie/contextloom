"""指标注册表测试。"""
from contextloom.observability.metrics import MetricsRegistry


def test_counter_and_timer():
    m = MetricsRegistry()
    m.incr("hits", 3)
    with m.time("op"):
        pass
    snap = m.snapshot()
    assert snap["counters"]["hits"] == 3
    assert "op" in snap["timings_ms"]
