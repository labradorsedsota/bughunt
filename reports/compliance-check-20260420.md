# BugHunt Result Cards 合规检查报告

> 检查时间：2026-04-20 11:45  
> 扫描范围：`results/` 全量  
> 文件总数：873 张  
> 检查标准：[worker-execution-guide.md](../worker-config/worker-execution-guide.md) JSON 格式规范

---

## 一、总览

| 指标 | 数值 |
|------|------|
| 总卡数 | 873 |
| 🔴 严重问题 | 52 处 |
| 🟡 警告 | 59 处 |
| 无问题卡 | ~780 张（89%） |

---

## 二、逐项检查结果

### 🔴 严重问题（必须修复）

| # | 检查项 | 问题数 | 状态 |
|---|--------|--------|------|
| 1 | JSON 可解析 | 0 | ✅ |
| 2 | 必填字段完整 | 4 | ❌ |
| 3 | status 值 ∈ {completed, failed} | 2 | ❌ |
| 4 | completed → mano_cua 完整（6 字段） | 0 | ✅ |
| 5 | mano_cua.result ∈ {normal, abnormal, unclear} | 0 | ✅ |
| 6 | completed → sess_id 格式合规 | 2 | ❌ |
| 7 | failed → failure 完整（4 字段） | 3 | ❌ |
| 9 | task_id 跨文件唯一 | 41 | ❌ |
| 11 | status 与 mano_cua.result 逻辑一致 | 0 | ✅ |

### 🟡 警告（建议修复）

| # | 检查项 | 问题数 | 状态 |
|---|--------|--------|------|
| 8 | failure.type 值合法 | 0 | ✅ |
| 10 | total_steps ≤ 80 | 37 | ⚠️ |
| 12 | expected_result_used 是 boolean | 0 | ✅ |
| 13 | duration_seconds 是数字 ≥ 0 | 0 | ✅ |
| 14 | timestamp 是 ISO 8601（含时区偏移） | 13 | ⚠️ |
| 15 | failed → mano_cua 为 null | 3 | ⚠️ |
| 16 | failed → sess_id 为 null | 6 | ⚠️ |
| 17 | repo 格式 owner/name | 0 | ✅ |
| 18 | failure.attempted 是数组 | 0 | ✅ |

---

## 三、问题明细

### #2 必填字段缺失（4 处）

全部来自同一张卡：

| 文件 | 缺失字段 |
|------|----------|
| worker-02/mint-ui-366.json | status, sess_id, expected_result_used, duration_seconds |

### #3 status 值非法（2 处）

| 文件 | 实际值 | 应为 |
|------|--------|------|
| worker-02/jodit-1335.json | `done` | completed 或 failed |
| worker-02/mint-ui-366.json | 无 | completed 或 failed |

### #6 sess_id 格式不合规（2 处）

合规格式：`sess-{14位数字时间戳}-{32位hex}`

| 文件 | 实际 sess_id |
|------|-------------|
| worker-01/apisix-dashboard-3321.json | `sess-20260419000014-apisix` |
| worker-01/mini-qr-219.json | `sess-20260419004700-miniqr` |

### #7 failed 卡 failure 字段不完整（3 处）

| 文件 | 缺失字段 |
|------|----------|
| worker-07/mint-ui-290.json | attempted, recommendation |
| worker-07/mint-ui-628.json | attempted, recommendation |
| worker-08/mint-ui-304.json | recommendation |

### #9 task_id 重复（41 组）

同一 task_id 出现在多个 worker 目录下：

| task_id | 重复位置 |
|---------|----------|
| BongoCat-431 | worker-02, worker-09, worker-fabrice（3份） |
| ByteStash-46 | worker-02, worker-03, worker-05（3份） |
| open5e-721 | worker-01, worker-02 |
| open5e-747 | worker-01, worker-02 |
| open5e-803 | worker-01, worker-02 |
| Analog-259 | worker-02, worker-03 |
| ByteStash-171 | worker-02, worker-03 |
| Dante-128 | worker-02, worker-fabrice |
| Piped-3715 | worker-02, worker-fabrice |
| cryptgeon-150 | worker-02, worker-06 |
| kan-206 | worker-02, worker-08 |
| kan-23 | worker-02, worker-06 |
| kan-242 | worker-02, worker-08 |
| kan-27 | worker-02, worker-08 |
| kan-30 | worker-02, worker-08 |
| medium-editor-1047 | worker-02, worker-fabrice |
| next-redux-wrapper-325 | worker-02, worker-03 |
| open5e-622 | worker-02, worker-07 |
| org-chart-69 | worker-02, worker-09 |
| slickgpt-38 | worker-02, worker-07 |
| ByteStash-157 | worker-03, worker-05 |
| ByteStash-58 | worker-03, worker-05 |
| Nucleus-26 | worker-03, worker-09 |
| editor-542 | worker-03, worker-09 |
| editor-893 | worker-03, worker-09 |
| emoji-mart-219 | worker-03, worker-06 |
| emoji-mart-254 | worker-03, worker-06 |
| emoji-mart-327 | worker-03, worker-06 |
| emoji-mart-762 | worker-03, worker-06 |
| kalendar-75 | worker-03, worker-09 |
| *（另有 11 组省略，完整列表见检查脚本输出）* | |

### #10 total_steps > 80（37 处）

| Worker | 文件 | 步数 |
|--------|------|------|
| worker-fabrice | batnoter-89.json | 216 |
| worker-03 | emoji-mart-218.json | 114 |
| worker-01 | ant-design-vue-7574.json | 112 |
| worker-02 | angular-datatables-1723.json | 110 |
| worker-05 | media-chrome-792.json | 109 |
| worker-07 | octo-76.json | 109 |
| worker-fabrice | Markpad-21.json | 101 |
| worker-07 | vue-hotel-datepicker-281.json | 100 |
| worker-02 | flitter-68.json | 99 |
| worker-05 | calendar-401.json | 99 |
| worker-02 | open5e-622.json | 97 |
| worker-01 | apisix-dashboard-3321.json | 94 |
| worker-04 | website-5102.json | 91 |
| *（另有 24 张在 81-90 步区间）* | |

### #14 timestamp 格式不合规（13 处）

全部来自 worker-04，使用 `Z`（UTC）结尾而非 `+08:00`：

| 文件 | 实际值 |
|------|--------|
| elements-874.json | `2026-04-18T04:56:00Z` |
| gateway-2079/2366/2940/3037/3122.json | `2026-04-18T04:50:00Z` |
| helpdesk-2669.json | `2026-04-18T04:57:00Z` |
| insights-647/744.json | `2026-04-18T04:55:00Z` |
| onlook-2574.json | `2026-04-18T04:58:00Z` |
| react-content-loader-93.json | `2026-04-17T06:16:00Z` |
| script-lab-623/648.json | `2026-04-17T08:47:00Z` / `09:16:00Z` |

### #15 failed 卡 mano_cua 非 null（3 处）

| 文件 | 说明 |
|------|------|
| worker-07/mint-ui-290.json | failed 但携带了 mano_cua 数据 |
| worker-07/mint-ui-628.json | 同上 |
| worker-08/mint-ui-304.json | 同上 |

### #16 failed 卡 sess_id 非 null（6 处）

| 文件 | sess_id |
|------|---------|
| worker-02/RapidRAW-658.json | sess-20260419181820-... |
| worker-02/multiple-select-355.json | sess-20260418234657-... |
| worker-05/BongoCat-438.json | sess-20260419010857-... |
| worker-06/ByteStash-173.json | sess-20260417225207-... |
| worker-06/editor-1842.json | sess-20260418234240-... |
| worker-08/mint-ui-304.json | sess-20260419182144-... |

> 注：这 6 张可能是 mano-cua 实际执行了但最终判定为 failed（如 timeout/url_deviation），sess_id 保留是合理的。建议放宽此项约束。

---

## 四、分 Worker 合规率

| Worker | 总卡数 | 问题处数 | 合规率 |
|--------|--------|----------|--------|
| worker-09 | 129 | 0 | **100%** |
| worker-03 | 98 | 2 | 98% |
| worker-06 | 80 | 2 | 98% |
| worker-08 | 101 | 3 | 97% |
| worker-01 | 75 | 5 | 93% |
| worker-05 | 82 | 10 | 88% |
| worker-07 | 68 | 8 | 88% |
| worker-02 | 127 | 17 | 87% |
| worker-fabrice | 64 | 9 | 86% |
| worker-04 | 49 | 14 | **71%** |

---

## 五、建议处理优先级

1. **#9 重复卡（41 组）** — 最高优先，需确定去重策略（保留哪个 worker 的结果）
2. **#2/#3 字段缺失/非法 status（3 张）** — 需 worker-02 补正
3. **#6 假 sess_id（2 张）** — 需重做（TOS 无对应轨迹）
4. **#7 failure 不完整（3 张）** — 需 worker-07/08 补充 attempted/recommendation
5. **#10 超步数（37 张）** — 数据可用但标注超限
6. **#14 timestamp Z 格式（13 张）** — worker-04 批量修正为 +08:00
