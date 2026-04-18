# worker-05 违规审计报告

> 生成时间：2026-04-18 10:37
> 规范依据：`worker-config/worker-execution-guide.md`

---

## 总览

| 指标 | 数值 |
|------|------|
| 结果文件总数 | 50 |
| 合规 | 42 (84.0%) |
| 不合规 | 8 (16.0%) |

### Status 分布

| status | 数量 | 合规 |
|--------|------|------|
| `completed` | 47 | ✅ |
| `failed` | 3 | ✅ |

### 违规类型汇总

| 类型 | 数量 |
|------|------|
| sess_id 问题 | 5 |
| mano_cua.result 非法值 | 5 |
| 缺少顶层必填字段 | 3 |
| failure 为 null | 3 |

---

## 不合规卡清单（8 张）

| # | 文件 | 问题 |
|---|------|------|
| 1 | `codeimage-420.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 2 | `codeimage-445.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 3 | `codeimage-641.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status=failed 但 failure 为 null |
| 4 | `lms-1931.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 5 | `lms-1932.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 6 | `lms-2098.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 7 | `svelte-splitpanes-3.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 8 | `think-83.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |

---

*报告由 Pichai 自动生成，数据截至 2026-04-18 10:37*
