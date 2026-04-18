# worker-07 违规审计报告

> 生成时间：2026-04-18 10:37
> 规范依据：`worker-config/worker-execution-guide.md`

---

## 总览

| 指标 | 数值 |
|------|------|
| 结果文件总数 | 43 |
| 合规 | 41 (95.3%) |
| 不合规 | 2 (4.7%) |

### Status 分布

| status | 数量 | 合规 |
|--------|------|------|
| `failed` | 25 | ✅ |
| `completed` | 16 | ✅ |
| `tool_error` | 1 | ❌ |
| `None` | 1 | ❌ |

### 违规类型汇总

| 类型 | 数量 |
|------|------|
| 缺少顶层必填字段 | 1 |
| status 非法值 | 1 |
| JSON 解析失败 | 1 |

---

## 不合规卡清单（2 张）

| # | 文件 | 问题 |
|---|------|------|
| 1 | `angular-calendar-1396.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `tool_error`（应为 completed/failed） |
| 2 | `react-date-picker-110.json` | JSON 解析失败: Invalid control character at: line 6 column 67 (char 197) |

---

*报告由 Pichai 自动生成，数据截至 2026-04-18 10:37*
