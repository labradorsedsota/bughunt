# worker-09 违规审计报告

> 生成时间：2026-04-18 10:37
> 规范依据：`worker-config/worker-execution-guide.md`

---

## 总览

| 指标 | 数值 |
|------|------|
| 结果文件总数 | 97 |
| 合规 | 68 (70.1%) |
| 不合规 | 29 (29.9%) |

### Status 分布

| status | 数量 | 合规 |
|--------|------|------|
| `failed` | 50 | ✅ |
| `completed` | 40 | ✅ |
| `None` | 7 | ❌ |

### 违规类型汇总

| 类型 | 数量 |
|------|------|
| 缺少顶层必填字段 | 23 |
| failure 为 null | 16 |
| status 非法值 | 7 |
| sess_id 问题 | 6 |

---

## 不合规卡清单（29 张）

| # | 文件 | 问题 |
|---|------|------|
| 1 | `Luckysheet-528.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds, timestamp<br>status 非法值: `None`（应为 completed/failed） |
| 2 | `Starkiller-5.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds, timestamp<br>status 非法值: `None`（应为 completed/failed） |
| 3 | `Task-Board-608.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds, timestamp<br>status 非法值: `None`（应为 completed/failed） |
| 4 | `devtools-598.json` | sess_id 缺失或为空 |
| 5 | `kaneo-1066.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 6 | `kaneo-1081.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 7 | `kaneo-1087.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 8 | `kaneo-1131.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 9 | `kaneo-1140.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 10 | `maker.js-556.json` | sess_id 缺失或为空 |
| 11 | `megadraft-283.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 12 | `megadraft-286.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 13 | `megadraft-288.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 14 | `megadraft-302.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 15 | `megadraft-319.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 16 | `megadraft-324.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 17 | `ngx-datatable-1702.json` | sess_id 缺失或为空 |
| 18 | `ngx-page-scroll-2.json` | sess_id 缺失或为空 |
| 19 | `openclaw-nerve-27.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 20 | `openclaw-nerve-64.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 21 | `react-grid-layout-918.json` | sess_id 缺失或为空 |
| 22 | `react-hot-toast-10.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 23 | `react-hot-toast-101.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 24 | `react-hot-toast-27.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 25 | `react-hot-toast-45.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 26 | `react-hot-toast-50.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 27 | `shadcn-solid-122.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 28 | `shadcn-solid-77.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 29 | `shikwasa-44.json` | sess_id 缺失或为空 |

---

*报告由 Pichai 自动生成，数据截至 2026-04-18 10:37*
