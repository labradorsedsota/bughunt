# worker-03 违规审计报告

> 生成时间：2026-04-18 10:37
> 规范依据：`worker-config/worker-execution-guide.md`

---

## 总览

| 指标 | 数值 |
|------|------|
| 结果文件总数 | 90 |
| 合规 | 63 (70.0%) |
| 不合规 | 27 (30.0%) |

### Status 分布

| status | 数量 | 合规 |
|--------|------|------|
| `completed` | 81 | ✅ |
| `failed` | 8 | ✅ |
| `None` | 1 | ❌ |

### 违规类型汇总

| 类型 | 数量 |
|------|------|
| 缺少顶层必填字段 | 25 |
| sess_id 问题 | 22 |
| mano_cua 缺字段 | 21 |
| failure 为 null | 4 |
| JSON 解析失败 | 1 |

---

## 不合规卡清单（27 张）

| # | 文件 | 问题 |
|---|------|------|
| 1 | `CopilotKit-3263.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 2 | `VueTorrent-2391.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 3 | `VueTorrent-2413.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 4 | `VueTorrent-2433.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 5 | `VueTorrent-2440.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 6 | `VueTorrent-2489.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 7 | `VueTorrent-2492.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 8 | `VueTorrent-2570.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 9 | `VueTorrent-2573.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 10 | `VueTorrent-2587.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 11 | `VueTorrent-2657.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 12 | `VueTorrent-2676.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 13 | `cboard-1752.json` | sess_id 格式错误: `sess-20260418000125-placeholder` |
| 14 | `cboard-2039.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 15 | `cloudinary-179.json` | 缺少顶层字段: sess_id, expected_result_used<br>status=failed 但 failure 为 null |
| 16 | `console-2604.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 17 | `devhub-107.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 18 | `open5e-622.json` | JSON 解析失败: Expecting property name enclosed in double quotes: line 16 column 137 (char 792) |
| 19 | `open5e-783.json` | 缺少顶层字段: sess_id, duration_seconds<br>status=failed 但 failure 为 null |
| 20 | `pluely-153.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 21 | `saleor-dashboard-5985.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 22 | `saltcorn-3596.json` | 缺少顶层字段: sess_id, duration_seconds<br>status=failed 但 failure 为 null |
| 23 | `saltcorn-3859.json` | 缺少顶层字段: sess_id, duration_seconds<br>status=failed 但 failure 为 null |
| 24 | `shopify-268.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 25 | `sim-3922.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 26 | `sim-3974.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |
| 27 | `wanderlust-392.json` | 缺少顶层字段: sess_id, duration_seconds<br>sess_id 缺失或为空<br>mano_cua 缺字段: total_steps, last_action, last_reasoning |

---

*报告由 Pichai 自动生成，数据截至 2026-04-18 10:37*
