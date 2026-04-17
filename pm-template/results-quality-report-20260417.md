# BugHunt Results 质量审查报告（2026-04-17）

> 统计时间：2026-04-17 15:10
> 
> 数据来源：results/ 目录全量扫描（335 个 JSON 文件）

---

## 一、总览

| 指标 | 值 |
|------|-----|
| result 文件总数 | 335 |
| JSON 可解析 | 334（1 个解析失败）|
| 有规范问题的卡 | 详见下方 |

---

## 二、Status 分布

| status | 数量 | 占比 | 是否标准 |
|--------|------|------|---------|
| completed | 250 | 74.6% | ✅ |
| failed | 59 | 17.6% | ✅ |
| deploy_failed | 13 | 3.9% | ❌ 非标准 |
| missing（无 status 字段）| 11 | 3.3% | ❌ 非标准 |
| unclear | 1 | 0.3% | ❌ 非标准 |
| blocked | 0 | 0% | ✅ |

### 非标准 status 明细

**deploy_failed（13 张）— 应归入 failed：**
- worker-03: open5e ×3
- worker-09: blinko ×5, organice ×5

**status 缺失（11 张）— 缺少顶层 status 字段：**
- worker-02: Semantic-UI-React ×5, react-content-loader ×1
- worker-03: emoji-mart ×5

**unclear（1 张）— 应归入 completed 并在 mano_cua.result 中标 unclear：**
- worker-09: rich-markdown-editor-489

---

## 三、Completed 卡的 mano_cua.result 分布

| result 类型 | 数量 | 占比 | 含义 |
|-------------|------|------|------|
| abnormal | 113 | 45.2% | 检测到 bug 行为 |
| unclear | 58 | 23.2% | 无法确认是否有 bug |
| normal | 55 | 22.0% | 未检测到 bug |
| deploy_failed | 22 | 8.8% | 部署失败（status=completed 但 result=deploy_failed）|
| bug_found | 1 | 0.4% | 明确发现 bug |
| missing | 1 | 0.4% | 无 result 字段 |

### ⚠️ 问题：22 张 status=completed 但 result=deploy_failed

这些卡的顶层 status 标为 completed，但 mano_cua.result 为 deploy_failed，逻辑矛盾。应该将 status 改为 failed。

---

## 四、mano_cua.total_steps 分布（227 张有步数数据）

| 步数区间 | 数量 | 占比 |
|----------|------|------|
| 1-20 步 | 63 | 27.8% |
| 21-40 步 | 52 | 22.9% |
| 41-60 步 | 54 | 23.8% |
| 61-80 步 | 39 | 17.2% |
| >80 步 | 19 | 8.4% |

- **最小**：3 步
- **最大**：151 步（worker-04/website-4780）
- **平均**：43 步
- **中位数**：40 步

### ⚠️ 超过 80 步上限的卡（19 张）

| Worker | task_id | 步数 | result |
|--------|---------|------|--------|
| worker-01 | TiddlyWiki5-9521 | 83 | abnormal |
| worker-01 | factoriolab-1295 | 90 | unclear |
| worker-01 | factoriolab-1332 | 116 | abnormal |
| worker-02 | learn.svelte.dev-360 | 86 | abnormal |
| worker-02 | medium-editor-1216 | 89 | unclear |
| worker-02 | tabler-react-134 | 90 | abnormal |
| worker-03 | editor.js-2084 | 113 | unclear |
| worker-03 | emoji-mart-218 | 95 | abnormal |
| worker-03 | svelte-typeahead-11 | 119 | abnormal |
| worker-04 | angular-datepicker-112 | 107 | unclear |
| worker-04 | website-4780 | 151 | abnormal |
| worker-04 | website-5102 | 91 | abnormal |
| worker-05 | editor.js-2536 | 106 | unclear |
| worker-05 | media-chrome-792 | 109 | abnormal |
| worker-05 | media-chrome-814 | 116 | normal |
| worker-05 | react-timeline-9000-200 | 88 | abnormal |
| worker-06 | typehero-1678 | 86 | unclear |
| worker-fabrice | betaflight-configurator-4900 | 114 | abnormal |
| worker-fabrice | vcal-340 | 98 | abnormal |

> 注：另有 worker-fabrice 的 vcal-342(84步) 和 vcal-352(86步) 也超过 80 步

---

## 五、Failed 卡的主要原因（59 张）

| 原因 | 数量 | 影响 Worker |
|------|------|------------|
| unknown（无失败原因记录）| 16 | worker-09 |
| 屏幕录制权限异常 | 5 | worker-01 |
| Next.js ERR_PACKAGE_PATH_NOT_EXPORTED | 4 | worker-09 |
| node-sass + Node 23 不兼容 | 3 | worker-09 |
| 需要 PostgreSQL 数据库 | 3 | worker-02 |
| Node.js 版本与 Svelte 不兼容 | 2 | worker-02 |
| PGLite 不支持（需真实 PostgreSQL）| 2 | worker-08 |
| OAuth 认证必须 | 2 | worker-09 |
| 其他（各 1 张）| 20 | 多个 |

---

## 六、sess_id 情况

**sess_id 在 result JSON 顶层**（不在 mano_cua 下面）。

| 情况 | 数量 |
|------|------|
| 顶层有 sess_id | 244 张 |
| 无 sess_id | 91 张 |

无 sess_id 的 91 张卡的 status 分布：
- failed: 52 张（部署失败等，未执行 mano-cua，无 session）
- completed: 14 张 ⚠️（已完成但缺 sess_id，需补录）
- deploy_failed: 13 张（非标准 status，部署失败无 session）
- missing: 11 张（缺 status 字段的卡）
- unclear: 1 张

**结论：** failed/deploy_failed 的卡无 sess_id 是合理的（未执行 mano-cua）。需关注的是 14 张 completed 但无 sess_id 的卡。

---

## 七、规范问题汇总

| 问题类型 | 数量 | 严重度 |
|----------|------|--------|
| mano_cua 缺 sess_id | — | — 已修正：sess_id 在顶层，非 mano_cua 下 |
| completed 但无 sess_id | 14 张 | 🟡 需补录 |
| status 非标准（deploy_failed/missing/unclear）| 25 张 | 🔴 需修正 |
| status=completed 但 result=deploy_failed | 22 张 | 🔴 逻辑矛盾 |
| mano_cua 缺 status/total_steps | 11 张 | 🟡 Semantic-UI-React + emoji-mart |
| total_steps > 80（超步数上限）| 19 张 | 🟡 数据可用但效率低 |

---

## 八、建议

1. **统一 status 值** — deploy_failed 归入 failed，unclear 归入 completed（在 mano_cua.result 中标注）
2. **修正 22 张 status=completed + result=deploy_failed 的矛盾卡**
3. **补全 11 张缺 status 的卡**（worker-02 Semantic-UI-React、worker-03 emoji-mart）
4. **排查 16 张 unknown 失败原因** — 全在 worker-09
5. **确认 sess_id 的标准字段路径** — 当前大量卡在 mano_cua 内但名称可能不一致
6. **强制 80 步硬切** — 19 张超步数卡说明 Worker 端未严格执行上限
