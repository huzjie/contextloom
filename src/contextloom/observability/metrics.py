"""轻量指标注册表。"""

from __future__ import annotations

import time
from collections import defaultdict


class MetricsRegistry:
    def __init__(self) -> None:
        self._counters: defaultdict[str, int] = defaultdict(int)
        self._timers: dict[str, list[float]] = defaultdict(list)

    def incr(self, name: str, value: int = 1) -> None:
        self._counters[name] += value

    def time(self, name: str):
        return _Timer(self, name)

    def record_timing(self, name: str, seconds: float) -> None:
        self._timers[name].append(seconds)

    def snapshot(self) -> dict:
        return {
            "counters": dict(self._counters),
            "timings_ms": {k: _avg(v) * 1000 for k, v in self._timers.items()},
        }


class _Timer:
    def __init__(self, registry: MetricsRegistry, name: str) -> None:
        self._r = registry
        self._name = name
        self._t0 = 0.0

    def __enter__(self):
        self._t0 = time.perf_counter()
        return self

    def __exit__(self, *exc):
        self._r.record_timing(self._name, time.perf_counter() - self._t0)
        return False


def _avg(vals: list[float]) -> float:
    return sum(vals) / len(vals) if vals else 0.0
