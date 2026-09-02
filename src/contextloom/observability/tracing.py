"""请求追踪工具。"""

from __future__ import annotations

import contextvars
import uuid

_trace_id: contextvars.ContextVar[str] = contextvars.ContextVar("trace_id", default="")


def start_trace() -> str:
    tid = uuid.uuid4().hex[:16]
    _trace_id.set(tid)
    return tid


def current_trace() -> str:
    return _trace_id.get()


def clear_trace() -> None:
    _trace_id.set("")
