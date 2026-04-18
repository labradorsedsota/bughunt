# worker-06 违规审计报告

> 生成时间：2026-04-18 10:37
> 规范依据：`worker-config/worker-execution-guide.md`

---

## 总览

| 指标 | 数值 |
|------|------|
| 结果文件总数 | 62 |
| 合规 | 57 (91.9%) |
| 不合规 | 5 (8.1%) |

### Status 分布

| status | 数量 | 合规 |
|--------|------|------|
| `completed` | 40 | ✅ |
| `failed` | 22 | ✅ |

### 违规类型汇总

| 类型 | 数量 |
|------|------|
| mano_cua.result 非法值 | 5 |
| sess_id 问题 | 4 |

---

## 不合规卡清单（5 张）

| # | 文件 | 问题 |
|---|------|------|
| 1 | `SvelteLab-194.json` | mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 2 | `mini-qr-59.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 3 | `monaco-editor-auto-typings-32.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 4 | `svelteui-283.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 5 | `svelteui-297.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |

---

*报告由 Pichai 自动生成，数据截至 2026-04-18 10:37*
