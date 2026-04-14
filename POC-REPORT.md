# BugHunt POC 报告

**执行时间：** 2026-04-14 13:47 — 22:51  
**范围：** 5 个项目 × 5 张卡 = 25 张  
**执行人：** Fabrice（lumen 5 + vcal 5）、Moss（multiple-select 5 + ha-fusion 5 + actual 5）  
**报告人：** Pichai  
**版本：** v1.1（2026-04-15 00:18 更新）

---

## 一、端到端流程验证

链路：任务卡（JSON）→ git clone + checkout buggy_commit → 部署 → mano-cua 执行 → sess_id → 结果 JSON → git push

| 环节 | 状态 |
|------|------|
| 任务卡读取 → 部署 | ✅ 通（4/5 项目成功部署） |
| mano-cua 启动 → 执行 | ✅ 通（18/25 卡成功启动执行） |
| sess_id 获取 | ✅ 通（21/25 有 sess_id） |
| 结果 JSON 生成 | ✅ 通（25/25 均产出标准格式 JSON） |
| git push 到 repo | ✅ 通（两个 Worker 结果均已提交） |

**结论：端到端链路跑通，核心数据流完整。**

---

## 二、执行结果明细

### 完成且有明确判定的卡（12 张）

| 卡 | Worker | 状态 | 判定 | 步数 | 耗时(s) | 关键信息 |
|---|---|---|---|---|---|---|
| ms-511 | Moss | COMPLETED | abnormal | 5 | 90 | 半选状态缺失 |
| ms-515 | Moss | COMPLETED | abnormal | 12 | 180 | 空 optgroup 导致 SelectAll 异常 |
| ms-607 | Moss | COMPLETED | abnormal | 10 | 120 | onFilter 大小写丢失 |
| ms-65 | Moss | COMPLETED | abnormal | 11 | 120 | filter 完全失效 |
| lumen-253 | Fabrice | COMPLETED | abnormal | 6 | 45 | 创建仓库报错 |
| vcal-340 | Fabrice | COMPLETED | abnormal | 98 | 1200 | 星期标题可点击无功能 |
| actual-5278 | Moss | COMPLETED | abnormal | 57 | 420 | 隐私模式余额悬停泄露 |
| ms-507 | Moss | COMPLETED | normal | 23 | 300 | dist 部署可能导致未复现 |
| lumen-149 | Fabrice | COMPLETED | normal | 243 | 3091 | 偏离任务做源码分析（异常值） |
| vcal-344 | Fabrice | COMPLETED | normal | 25 | 240 | 月份导航正常 |
| vcal-350 | Fabrice | COMPLETED | normal | 76 | 720 | 日期高亮正常 |
| actual-7282 | Moss | COMPLETED | unclear | 64 | 900 | bank sync 需后端，无法进入测试 |

### mano-cua 执行了但未完成的卡（6 张）

| 卡 | Worker | 原因 | 步数 | 耗时(s) |
|---|---|---|---|---|
| lumen-300 | Fabrice | 残留登录态 → 502 崩溃 | 167 | 1789 |
| lumen-451 | Fabrice | Terminal 逃逸 | 50 | 972 |
| lumen-473 | Fabrice | 残留态 + DevTools 被阻 | 56 | 960 |
| vcal-342 | Fabrice | 找不到 input mode → Terminal 逃逸 | 84 | 925 |
| vcal-352 | Fabrice | Terminal 逃逸分析 CSS | 86 | 960 |
| actual-5481 | Moss | 步数过多被中止，过程中发现额外 bug | 68 | 900 |

### 失败（mano-cua 未能有效执行）的卡（7 张）

| 卡 | Worker | 类型 |
|---|---|---|
| ha-fusion-62/220/278/476/478 | Moss | PROJECT_BLOCKED，需 HA 后端认证 |
| actual-7332 | Moss | mano-cua session 反复中止（0/1/9 步） |
| actual-7475 | Moss | mano-cua session 初始化即中止 |

---

## 三、关键指标

| 指标 | 数值 |
|------|------|
| 有效复现率 | 7/11 = **64%**（abnormal / 有明确判定的卡，排除 unclear） |
| mano-cua 启动成功率 | 18/25 = **72%** |
| 项目级部署失败率 | 1/5 = **20%**（仅 ha-fusion） |
| 卡级 BLOCKED 率 | 5/25 = **20%** |
| mano-cua 系统错误率 | 2/25 = **8%** |

---

## 四、单 case 耗时基线（修正版）

> ⚠️ 以下为完整生命周期耗时（含 clone、部署、执行、结果处理），非仅 mano-cua 执行时间。

### 墙钟时间统计

| Worker | 项目 | 卡数 | 墙钟时间 | 平均每张 |
|--------|------|------|---------|---------|
| Fabrice | lumen | 5 | 143 min | 28.6 min |
| Fabrice | vcal | 5 | 99 min | 19.8 min |
| Moss | multiple-select | 5 | 20 min | 4.0 min |
| Moss | ha-fusion | 5 | ~5 min | ~1 min（快速 BLOCKED） |
| Moss | actual | 5 | 64 min | 12.8 min |

### 产能基线

| 场景 | 实际耗时 | 产能 |
|------|---------|------|
| 同项目连续执行（最优） | 4 分钟/张 | ~15 张/小时 |
| 含项目切换（正常） | 15-27 分钟/张 | ~2-4 张/小时 |
| 整体加权平均 | ~16 分钟/张 | **~3-4 张/小时/Worker** |

---

## 五、暴露的问题与应对

| 问题 | 严重程度 | 影响 | 应对措施 | 负责人 | 状态 |
|------|---------|------|---------|--------|------|
| ha-fusion 需后端认证 | 高 | 筛选假阳性 | 管线加后端依赖黑名单检测 | 智子 | ✅ 已修 |
| mano-cua Terminal 逃逸（3 张） | 高 | 无效数据消耗步数 | 任务卡加 Level B 引导语 + 执行手册加浏览器边界约束 | 智子 + Pichai | ✅ 已修 |
| 浏览器残留状态（2 张） | 中 | 上一个 case 污染下一个 | 📋 **待确认**：方案 A（Chrome 隐身模式，一行改动但需验证 mano-cua 兼容性）或方案 B（pm-cockpit 模式，打开页面后 localStorage.clear + reload）。林菡要求先记下待定 | Pichai | 📋 待确认 |
| mano-cua session 不稳定（2 张） | 中 | 执行中断 | mano-cua 工具层面问题，非本项目范围 | — | ⚠️ 已知风险，无应对 |
| dist 部署 vs dev 模式（1 张） | 中 | 未复现 | deploy_commands 统一 `npm run dev` | 智子 | ✅ 已修 |
| lumen-149 跑 243 步无干预 | 中 | 时间浪费 | 步数上限 80 步已落地 | Pichai | ✅ 已修（林菡确认） |
| PM 巡检数据不准 | 高 | 进度失控 | 📋 **待改进**：具体改进方案和验收标准尚未确定。初步方向：memory 必须落盘、巡检频率提高、自动化巡检 | Pichai | 📋 待制定方案 |
| 管线框架/库混入（验证后发现） | 高 | 批量产卡命中大量不可部署的框架项目 | 📋 **待修**：智子管线需区分"框架/库"和"可部署应用"（TanStack/query、angular/angular 等被错误选入） | 智子 | 🔧 修复中 |

---

## 六、对任务卡的修改需求（已落地 / 待落地）

| 修改项 | 优先级 | 状态 | 确认情况 |
|--------|--------|------|---------|
| 结果 JSON 加 `repo` 字段 | P0 | 📋 待执行 | ✅ 林菡确认可加。**Pichai 尚未更新到执行手册 JSON 模板** |
| deploy_commands 强制 `npm run dev` | P0 | ✅ 已修 | ✅ 智子管线已改 |
| 管线排除后端认证项目 | P0 | ✅ 已修 | ✅ 智子管线已改 |
| test_page Level A + Level B 引导语 | P0 | ✅ 已修 | ✅ 智子管线已改 + Pichai 执行手册已加浏览器边界约束 |
| 执行手册加浏览器边界约束 | P0 | ✅ 已修 | ✅ 林菡确认，已 push |
| `expected_result_used` 字段 | P1 | ✅ POC 结果已有 | ❓ 未正式写入执行手册 JSON 模板 |
| log 文件 push 到 repo | P1 | 📋 待评估 | ❓ 无明确评估标准和时间点，智子 P1 请求 |
| `deploy_notes` 字段 | P2 | 📋 待评估 | ❓ Pichai 建议，林菡未确认是否需要 |
| Worker 术语 → FTY 术语映射 | P0 | 📋 待对齐 | ❓ Emily 确认由她来对齐 FTY。`unclear → 部分复现` 语义是否准确待确认 |

---

## 七、Worker 部署失败后的自主恢复

**关键发现：** actual 项目最初被认为"全部部署失败"，但 Moss 自主调整部署策略后成功执行 3/5 张卡（含 actual-5278 发现真实 bug）。

**Take-away：**
1. Worker 自主排障能力直接影响产出量
2. 📋 **待确认**：执行手册的 PROJECT_BLOCKED 规则是否调整为"先尝试至少 1 种替代策略再上报"（Pichai 建议，林菡未确认）
3. 📋 **待确认**：成功的变通策略是否需要回流记录（建议加 `deploy_notes` 字段，林菡未确认）
4. 折损率不是固定值——Worker 越强，折损越低

---

## 八、总结

POC 验证了 BugHunt 端到端链路可行，核心数据流完整。5 个项目中 4 个成功部署执行，有效复现率 64%。

**主要风险：**
- 筛选质量（ha-fusion 类假阳性）→ 智子已修管线
- mano-cua 行为稳定性（Terminal 逃逸）→ 双保险约束已加
- 浏览器状态隔离 → 待正式执行前确认方案
- PM 巡检准确性 → 需改进 memory 落盘和巡检频率

**产能预期：** 3-4 张/小时/Worker（含完整生命周期），同项目连续执行可达 15 张/小时。
