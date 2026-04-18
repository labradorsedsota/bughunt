# worker-01 违规审计报告

> 生成时间：2026-04-18 10:37
> 规范依据：`worker-config/worker-execution-guide.md`

---

## 总览

| 指标 | 数值 |
|------|------|
| 结果文件总数 | 57 |
| 合规 | 41 (71.9%) |
| 不合规 | 16 (28.1%) |

### Status 分布

| status | 数量 | 合规 |
|--------|------|------|
| `completed` | 49 | ✅ |
| `failed` | 8 | ✅ |

### 违规类型汇总

| 类型 | 数量 |
|------|------|
| sess_id 问题 | 11 |
| mano_cua.result 非法值 | 11 |
| failure.type 非法值 | 4 |

---

## 不合规卡清单（16 张）

| # | 文件 | 问题 |
|---|------|------|
| 1 | `Semantic-UI-React-3502.json` | failure.type 非法值: `deploy_blocked` |
| 2 | `Semantic-UI-React-3552.json` | failure.type 非法值: `deploy_blocked` |
| 3 | `Semantic-UI-React-3581.json` | failure.type 非法值: `deploy_blocked` |
| 4 | `Semantic-UI-React-3669.json` | failure.type 非法值: `deploy_blocked` |
| 5 | `animate-ui-129.json` | sess_id 格式错误: `sess-20260417184505-417183909-4fe90955a8a841be8809c20c50b9bc63` |
| 6 | `devhub-17.json` | mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 7 | `docz-985.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 8 | `photon-330.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 9 | `photon-526.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 10 | `shopify-223.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 11 | `shopify-259.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 12 | `shopify-264.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 13 | `shopify-267.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 14 | `shopify-269.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 15 | `shopify-274.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |
| 16 | `shopify-293.json` | sess_id 缺失或为空<br>mano_cua.result 非法值: `deploy_failed`（应为 normal/abnormal/unclear） |

---

*报告由 Pichai 自动生成，数据截至 2026-04-18 10:37*
