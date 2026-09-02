"""追踪测试。"""
from contextloom.observability.tracing import clear_trace, current_trace, start_trace


def test_trace():
    tid = start_trace()
    assert current_trace() == tid
    clear_trace()
    assert current_trace() == ""
