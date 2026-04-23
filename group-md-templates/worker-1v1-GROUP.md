# GROUP.md - BugHunt 工作群 (PM ↔ Worker)

## 群定位
PM 与该 Worker 的专属工作通道。**Worker 的唯一信息源。**
任务分发、状态上报、异常处理、方案变更通知——所有影响执行的信息都从这里获取。

## 成员
- **PM (Pichai)**：选卡排产、巡检、干预指令、方案变更推送
- **Mycroft**：任务分发
- **Worker ({worker名})**：执行任务、上报状态

## ⚠️ 核心规则：所有汇报必须 @Pichai

Worker 发送的所有状态信号、ACK、异常上报、闭环汇总，**必须 @Pichai（消息中带 mention 字段）**。
不带 @Pichai 的消息 PM 收不到，等于没发。

## 通信协议

### Mycroft → Worker：任务分发
Mycroft 发送任务批次，Worker 收到后 @Pichai 回复 ACK 后开始执行。
```
📋 第 N 批任务（共 X 张）

任务列表：
1. luxesite-253
2. luxesite-258
3. cleaningsvc-18

执行手册：worker-config/worker-execution-guide.md（repo 里 pull 最新版）
任务卡位置：tasks/pool-clean/ 下对应 JSON 文件
结果输出：results/{worker名}/

同项目多张卡共享 clone + install，只需切换 buggy_commit。
```

### PM → Worker：方案变更
全局方案变更由 PM 在本群直接推送（不从其他群获取）。
```
⚠️ 方案变更
内容: 结果 JSON 新增 repo 字段，从任务卡原样复制
生效: 立即，下一个 case 开始执行
影响: completed 和 failed 两种格式都要加
```

### PM → Worker：干预指令
```
🛑 暂停执行（取消当前任务，等待新指令）
▶️ 恢复执行（继续之前的任务列表）
⏭️ 跳过当前 case（标 failed + other，进入下一个）
```

### Worker → PM：ACK 确认
**收到任务后立刻 @Pichai 确认：**
```
@Pichai 收到，开始执行第 N 批
```

### Worker → PM：状态上报
**每完成一个 case，立刻 @Pichai 发一行状态信号：**
```
@Pichai ✅ luxesite-253 | 4m32s | abnormal | 404页面无返回链接
@Pichai ❌ cleaningsvc-18 | deploy_failed | npm install node-gyp 编译错误
@Pichai ⚠️ lumen-300 | 12m10s | unclear | mano-cua 未走到关键步骤
```

### Worker → PM：异常上报
**遇异常超 10 分钟解决不了 → 立即 @Pichai 报异常：**
- 失败现象
- 已尝试的方案
- 建议

### Worker → PM：批次完成闭环
**当前批次全部完成后 → @Pichai 闭环汇报：**
```
@Pichai 第 N 批完成，X✅ Y❌ Z⚠️，结果已 push，请派下一批
```
- 如果 @Pichai 后 10 分钟无响应，再 @ 一次

### Worker → Repo：结果持久化
- 每完成 5 个 case，批量 git push 结果 JSON 到 `results/{worker名}/`
- 异常 case 立刻 push，不等凑批

## Worker 行为规范
1. 收到任务 → **@Pichai** 回复"收到，开始执行第 N 批"（ACK）
2. 每完成一个 case → **@Pichai** 发状态信号（不等 PM 来问）
3. **每个 case 必须在独立 turn 中完成** — 部署 → mano-cua → 写结果 → @Pichai 发状态 → 结束当前 turn → 下一个 turn 再开始下一个 case。禁止一个 turn 内连续执行多个 case
4. 遇到异常超 10 分钟解决不了 → **@Pichai** 立即上报 + 诊断
5. 超过 15 分钟没产出 → **@Pichai** 主动说明原因（部署慢 / mano-cua 执行中 / 卡住了）
6. 当前批次全部完成 → **@Pichai** 报闭环汇总 + "请派下一批"
7. 收到 PM 的暂停/跳过/切换任务等指令 → **@Pichai** 回复 ACK + 执行
8. 收到方案变更 → **@Pichai** 回复"收到，已更新" + 从下一个 case 生效

**关键：不带 @Pichai 的消息 PM 收不到，等于没发。**

## PM 行为规范
1. 分发任务时给明确列表，不说模糊的"继续跑"
2. 巡检时如果 Worker 超过 20 分钟没信号 → 主动询问
3. 干预指令必须明确：作废旧指令 + 新指令内容
4. 全局方案变更 → 在每个 1v1 群逐个推送（不依赖广播群）
5. Worker @Pichai 报"请派下一批"后 → 10 分钟内派发下一批或回复说明

## 禁止
- Worker 不在此群讨论与自己任务无关的内容
- PM 不在此群发与该 Worker 无关的其他 Worker 信息
