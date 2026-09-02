"""上下文装配器：token 预算管理，把检索片段装入长上下文窗口。"""

from __future__ import annotations

import re

from contextloom.core.models import SearchResult

_SYSTEM = (
    "你是 ContextLoom 的文档智能助手。请基于【参考材料】回答用户问题。\n"
    "要求：\n"
    "1. 参考材料足够时给出明确完整结论并注明依据。\n"
    "2. 材料不足时明确说明缺失信息。\n"
    "3. 涉及跨章节规则时综合多段材料判断。\n"
    "4. 用简体中文回答。"
)


class ContextAssembler:
    def __init__(self, context_window: int = 131072, reserve_ratio: float = 0.5) -> None:
        self.context_window = context_window
        self.reserve_ratio = reserve_ratio

    def build_prompt(self, question: str, results: list[SearchResult]) -> tuple[str, str]:
        budget = int(self.context_window * self.reserve_ratio)
        sections: list[str] = []
        used = 0
        seen: set[str] = set()
        for r in results:
            if r.text in seen:
                continue
            seen.add(r.text)
            heading = f"[{r.heading}] " if r.heading else ""
            block = f"【片段】{heading}{r.text}\n"
            approx = len(block) // 4 + block.count("。")
            if used + approx > budget:
                break
            sections.append(block)
            used += approx
        material = "\n".join(sections) if sections else "（无参考材料）"
        prompt = (f"【用户问题】\n{question}\n\n"
                  f"【参考材料】\n{material}\n\n请基于以上参考材料回答。")
        return _SYSTEM, prompt

    def estimate_tokens(self, text: str) -> int:
        cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
        return cjk + max(1, (len(text) - cjk) // 4)
