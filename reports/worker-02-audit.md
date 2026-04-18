# worker-02 违规审计报告

> 生成时间：2026-04-18 10:37
> 规范依据：`worker-config/worker-execution-guide.md`

---

## 总览

| 指标 | 数值 |
|------|------|
| 结果文件总数 | 127 |
| 合规 | 50 (39.4%) |
| 不合规 | 77 (60.6%) |

### Status 分布

| status | 数量 | 合规 |
|--------|------|------|
| `completed` | 39 | ✅ |
| `None` | 33 | ❌ |
| `failed` | 16 | ✅ |
| `abnormal` | 14 | ❌ |
| `error` | 9 | ❌ |
| `unclear` | 7 | ❌ |
| `deploy_failed` | 5 | ❌ |
| `normal` | 4 | ❌ |

### 违规类型汇总

| 类型 | 数量 |
|------|------|
| 缺少顶层必填字段 | 72 |
| status 非法值 | 72 |
| failure 为 null | 3 |
| sess_id 问题 | 2 |
| mano_cua 缺字段 | 2 |

---

## 不合规卡清单（77 张）

| # | 文件 | 问题 |
|---|------|------|
| 1 | `Analog-259.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `error`（应为 completed/failed） |
| 2 | `BongoCat-431.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `error`（应为 completed/failed） |
| 3 | `BongoCat-437.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `error`（应为 completed/failed） |
| 4 | `BongoCat-438.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `error`（应为 completed/failed） |
| 5 | `BongoCat-499.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `error`（应为 completed/failed） |
| 6 | `BongoCat-509.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `error`（应为 completed/failed） |
| 7 | `BongoCat-592.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `error`（应为 completed/failed） |
| 8 | `BongoCat-777.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `error`（应为 completed/failed） |
| 9 | `ByteStash-156.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 10 | `ByteStash-157.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 11 | `ByteStash-171.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 12 | `ByteStash-173.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 13 | `ByteStash-46.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 14 | `ByteStash-58.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 15 | `Dante-128.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `error`（应为 completed/failed） |
| 16 | `Luckysheet-528.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `unclear`（应为 completed/failed） |
| 17 | `Markpad-21.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `unclear`（应为 completed/failed） |
| 18 | `Notpad-195.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 19 | `Notpad-268.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 20 | `Semantic-UI-React-3864.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `normal`（应为 completed/failed） |
| 21 | `Semantic-UI-React-3994.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `normal`（应为 completed/failed） |
| 22 | `Semantic-UI-React-4005.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 23 | `Semantic-UI-React-4083.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `unclear`（应为 completed/failed） |
| 24 | `Semantic-UI-React-4110.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `unclear`（应为 completed/failed） |
| 25 | `Silex-743.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 26 | `Silex-843.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 27 | `angular-datatables-1605.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 28 | `angular-datatables-1723.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 29 | `angular-datepicker-112.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 30 | `angular-gridster2-377.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 31 | `angular-gridster2-529.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 32 | `cryptgeon-150.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 33 | `emoji-mart-218.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 34 | `emoji-mart-219.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 35 | `emoji-mart-220.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `unclear`（应为 completed/failed） |
| 36 | `emoji-mart-254.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `normal`（应为 completed/failed） |
| 37 | `emoji-mart-327.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 38 | `emoji-mart-762.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `unclear`（应为 completed/failed） |
| 39 | `flitter-68.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 40 | `kan-206.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 41 | `kan-23.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 42 | `kan-242.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 43 | `kan-27.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 44 | `kan-30.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 45 | `kan-35.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 46 | `kan-70.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 47 | `karakeep-2395.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `deploy_failed`（应为 completed/failed） |
| 48 | `karakeep-2396.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `deploy_failed`（应为 completed/failed） |
| 49 | `karakeep-2493.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `deploy_failed`（应为 completed/failed） |
| 50 | `next-redux-wrapper-325.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 51 | `onlook-2587.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 52 | `onlook-2908.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 53 | `open5e-622.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 54 | `open5e-655.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 55 | `open5e-694.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 56 | `open5e-695.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 57 | `open5e-716.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 58 | `open5e-721.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 59 | `open5e-747.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 60 | `open5e-775.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 61 | `open5e-799.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 62 | `open5e-803.json` | 缺少顶层字段: repo, status, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 63 | `padloc-427.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 64 | `padloc-638.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 65 | `script-lab-667.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 66 | `script-lab-672.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 67 | `script-lab-732.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `abnormal`（应为 completed/failed） |
| 68 | `shopware-pwa-1537.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `deploy_failed`（应为 completed/failed） |
| 69 | `shopware-pwa-1665.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `deploy_failed`（应为 completed/failed） |
| 70 | `signature_pad-120.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `normal`（应为 completed/failed） |
| 71 | `signature_pad-656.json` | 缺少顶层字段: sess_id, expected_result_used, duration_seconds<br>status 非法值: `unclear`（应为 completed/failed） |
| 72 | `slickgpt-38.json` | 缺少顶层字段: status, sess_id, expected_result_used, duration_seconds<br>status 非法值: `None`（应为 completed/failed） |
| 73 | `vue-pdf-179.json` | sess_id 格式错误: `N/A-code-review`<br>mano_cua 缺字段: last_reasoning |
| 74 | `vue-pdf-189.json` | sess_id 格式错误: `N/A-code-review`<br>mano_cua 缺字段: last_reasoning |
| 75 | `website-4566.json` | status=failed 但 failure 为 null |
| 76 | `website-4776.json` | status=failed 但 failure 为 null |
| 77 | `website-4780.json` | status=failed 但 failure 为 null |

---

*报告由 Pichai 自动生成，数据截至 2026-04-18 10:37*
