"""Token 估算工具。"""

from __future__ import annotations

import re

_CJK = re.compile(r"[\u4e00-\u9fff]")


def estimate_tokens(text: str) -> int:
    cjk = len(_CJK.findall(text))
    other = len(text) - cjk
    return max(1, cjk + other // 4)


def truncate_to_tokens(text: str, budget: int) -> str:
    if estimate_tokens(text) <= budget:
        return text
    lo, hi = 0, len(text)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if estimate_tokens(text[:mid]) <= budget:
            lo = mid
        else:
            hi = mid - 1
    return text[:lo]
