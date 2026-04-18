# worker-04 违规审计报告

> 生成时间：2026-04-18 10:37
> 规范依据：`worker-config/worker-execution-guide.md`

---

## 总览

| 指标 | 数值 |
|------|------|
| 结果文件总数 | 55 |
| 合规 | 49 (89.1%) |
| 不合规 | 6 (10.9%) |

### Status 分布

| status | 数量 | 合规 |
|--------|------|------|
| `completed` | 47 | ✅ |
| `failed` | 8 | ✅ |

### 违规类型汇总

| 类型 | 数量 |
|------|------|
| sess_id 问题 | 6 |
| 缺少顶层必填字段 | 5 |
| mano_cua 为 null | 5 |

---

## 不合规卡清单（6 张）

| # | 文件 | 问题 |
|---|------|------|
| 1 | `react-content-loader-93.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>sess_id 缺失或为空<br>status=completed 但 mano_cua 为 null |
| 2 | `script-lab-609.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>sess_id 缺失或为空<br>status=completed 但 mano_cua 为 null |
| 3 | `script-lab-623.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>sess_id 缺失或为空<br>status=completed 但 mano_cua 为 null |
| 4 | `script-lab-648.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>sess_id 缺失或为空<br>status=completed 但 mano_cua 为 null |
| 5 | `svelte-tags-input-17.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>sess_id 缺失或为空<br>status=completed 但 mano_cua 为 null |
| 6 | `website-4885.json` | sess_id 缺失或为空 |

---

*报告由 Pichai 自动生成，数据截至 2026-04-18 10:37*
