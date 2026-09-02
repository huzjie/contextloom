# 可观测性

- 指标：`MetricsRegistry` 提供计数器与耗时统计。
- 追踪：`start_trace()` / `current_trace()` 传递 trace id。
- 中间件：`TimingMiddleware` 自动注入 `X-Process-Time-Ms` 响应头。
