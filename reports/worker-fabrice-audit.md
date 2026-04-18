# worker-fabrice 违规审计报告

> 生成时间：2026-04-18 10:37
> 规范依据：`worker-config/worker-execution-guide.md`

---

## 总览

| 指标 | 数值 |
|------|------|
| 结果文件总数 | 51 |
| 合规 | 31 (60.8%) |
| 不合规 | 20 (39.2%) |

### Status 分布

| status | 数量 | 合规 |
|--------|------|------|
| `failed` | 30 | ✅ |
| `completed` | 21 | ✅ |

### 违规类型汇总

| 类型 | 数量 |
|------|------|
| 缺少顶层必填字段 | 16 |
| failure 为 null | 13 |
| mano_cua 缺字段 | 6 |
| sess_id 问题 | 4 |

---

## 不合规卡清单（20 张）

| # | 文件 | 问题 |
|---|------|------|
| 1 | `Notpad-195.json` | mano_cua 缺字段: status, last_action, last_reasoning |
| 2 | `PeaNUT-35.json` | mano_cua 缺字段: status, last_action, last_reasoning |
| 3 | `Piped-3715.json` | mano_cua 缺字段: status, last_action, last_reasoning |
| 4 | `accounts-ui-173.json` | sess_id 格式错误: `sess-accounts-ui-173` |
| 5 | `accounts-ui-191.json` | 缺少顶层字段: sess_id<br>sess_id 缺失或为空<br>mano_cua 缺字段: last_action, last_reasoning |
| 6 | `accounts-ui-203.json` | 缺少顶层字段: sess_id<br>sess_id 缺失或为空<br>mano_cua 缺字段: last_action, last_reasoning |
| 7 | `accounts-ui-204.json` | 缺少顶层字段: sess_id<br>sess_id 缺失或为空<br>mano_cua 缺字段: last_action, last_reasoning |
| 8 | `commercejs-nextjs-demo-store-130.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 9 | `commercejs-nextjs-demo-store-156.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 10 | `commercejs-nextjs-demo-store-175.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 11 | `commercejs-nextjs-demo-store-221.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 12 | `commercejs-nextjs-demo-store-40.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 13 | `commercejs-nextjs-demo-store-59.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 14 | `commercejs-nextjs-demo-store-85.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 15 | `commercejs-nextjs-demo-store-88.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 16 | `commercejs-nextjs-demo-store-93.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 17 | `nuxt-studio-149.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 18 | `nuxt-studio-81.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 19 | `photon-342.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 20 | `photon-478.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |

---

*报告由 Pichai 自动生成，数据截至 2026-04-18 10:37*
