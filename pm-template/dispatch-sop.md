# 派发工作 SOP

> 本文档描述任务派发的完整工作方法和职责分工。

---

## 一、职责分工

| 职责 | 负责人 | 说明 |
|------|--------|------|
| 选卡、排产 | Pichai | 决定哪个 Worker 跑哪些卡，写入 dispatch-log |
| 发送派发消息 | Mycroft | 读 dispatch-log，按模板发消息到 Worker 1v1 通道 |
| 维护 dispatch-log | Pichai | 更新状态、记录结果 |
| 异常处理 | Pichai | Worker 报异常时判断和干预 |
| 巡检 | Pichai | 监控 Worker 进度，催促无响应的 Worker |

### 工作流

```
Pichai 选卡 → 写入 dispatch-log 并 push
    ↓
Mycroft 读 dispatch-log → 按模板发消息给 Worker
    ↓
Worker ACK / 状态信号 → @Pichai
    ↓
Pichai 更新 dispatch-log → 批次完成后选下一批 → 循环
```

---

## 二、Pichai 的工作：选卡与写入 dispatch-log

### 2.1 选卡规则

- **数据来源**：`tasks/pool/`（727 张完整卡，含 ground_truth）+ `pm-template/dispatch-log.md`（已派发记录）
- **发给 Worker 的卡**：从 `tasks/pool-clean/` 读取（不含 ground_truth）
- **不重复派发** — 跳过 dispatch-log 中已有的 task_id
- **纯净卡优先** — 优先选 `backend_risk` 为 false 或不存在的卡
- **同项目同 Worker** — 同 repo 的卡分给同一个 Worker，复用部署
- **每批 5 张**
- **均匀分配** — 多 Worker 同时派发时卡数相等

### 2.2 写入 dispatch-log 的格式

Pichai 选好卡后，在 dispatch-log.md 中追加记录：

```markdown
### [时间] 第 N 批 → worker-XX

**状态：** 待 Mycroft 发送

**任务列表：**
1. task_id_1 — 🔲 待执行
2. task_id_2 — 🔲 待执行
3. task_id_3 — 🔲 待执行
4. task_id_4 — 🔲 待执行
5. task_id_5 — 🔲 待执行

**进度：** 0/5 完成
**备注：** 同项目 xxx，共享部署
```

同时更新总览表，push 到 repo。

---

## 三、Mycroft 的工作：发送派发消息

### 3.1 触发条件

dispatch-log.md 中出现状态为 **「待 Mycroft 发送」** 的记录时，执行发送。

### 3.2 Worker 1v1 通道

| Worker | Channel ID | UID |
|--------|-----------|-----|
| worker-01 | c7b092f81af944a286e1dd631038c4aa | worker01_bot |
| worker-02 | c6288de9437d4dbaa5d6a66573578b95 | worker02_bot |
| worker-03 | f72274d28dc740efb7805f70fd5bb3b3 | worker03_bot |
| worker-04 | 6d7d933c594044a688484ca815c06433 | worker04_bot |
| worker-05 | d94fe49dfeec4d52b491eb6b0479256b | worker05_bot |
| worker-06 | fcb1cd72ae25476ab713568df49fe2db | worker06_bot |
| worker-07 | 13aea54f953c4a53bac98d995a33c111 | worker07_bot |
| worker-08 | 1147ef05c926437ab28936d92fcc0590 | worker08_bot |
| worker-09 | 5c49656f14114b6285b0c32e6e6bff4e | worker09_bot |
| worker-fabrice | 44998d9add6d40b287a38332cbaf61ca | hermes_bot |

### 3.3 每个 Worker 发送 3 类消息

**顺序严格：指令 → 规则 → 逐张卡 JSON。每条间隔 200-300ms。**

---

**第 1 条：派发指令**（必须 @Worker，payload 带 mention 字段）

```
@{worker名} 📋 第 {N} 批任务（共 {X} 张）

任务列表：
1. {task_id_1}
2. {task_id_2}
...

执行手册：worker-config/worker-execution-guide.md（repo 里 pull 最新版）
任务卡位置：tasks/pool-clean/ 下对应 JSON 文件（不含 ground_truth）
结果输出：results/{worker-XX}/

同项目多张卡共享 clone + install，只需切换 buggy_commit。
```

---

**第 2 条：汇报规则**（不需要 mention）

```
⚠️ 汇报规则（必须遵守）：

1. 收到任务 → @Pichai 回复"收到，开始执行第 {N} 批"
2. 每完成 1 个 case → @Pichai 发状态（✅/❌/⚠️ task_id | 耗时 | 判定 | 摘要）
3. 遇异常超 10 分钟解决不了 → @Pichai 报异常
4. 全批完成 → @Pichai 报"第 {N} 批完成，X✅ Y❌ Z⚠️，结果已 push，请派下一批"
5. ⚠️ 每个 case 完成 mano-cua 后，先发状态信号再开始下一个 case，不要一口气跑完再汇报
6. 所有汇报消息必须 @Pichai（带 mention 字段），否则 PM 收不到

现在请先 @Pichai 回复 ACK。
```

---

**第 3-7 条：逐张发任务卡 JSON**（不需要 mention）

从 `tasks/pool-clean/{task_id}.json` 读取 JSON（**不含 ground_truth**），每张卡一条消息：

```
📄 任务卡 {序号}/{总数}: {task_id}

{完整 JSON 内容，pretty-print}
```

---

### 3.4 发送 API

```bash
curl -s -X POST "https://im.deepminer.com.cn/api/v1/bot/sendMessage" \
  -H "Authorization: Bearer bf_f44080a9a3d4b527b2ab93c42dc9571c" \
  -H "Content-Type: application/json" \
  -d '{
    "channel_id": "{channel_id}",
    "channel_type": 2,
    "payload": {
      "type": 1,
      "content": "消息内容",
      "mention": {"uids": ["{worker_uid}"]}
    }
  }'
```

- channel_type 固定为 2（群聊）
- mention 字段只在第 1 条消息（@Worker）时需要

### 3.5 发送完成后

更新 dispatch-log 中对应记录的状态：「待 Mycroft 发送」→「已派发，等待 ACK」，push。

---

## 四、状态流转

```
待 Mycroft 发送 → 已派发，等待 ACK → ACK已确认，执行中 → 已完成
```

每个 task_id 的状态标记：
- 🔲 待执行
- ⏳ 执行中
- ✅ abnormal/normal（+ 耗时 + 摘要）
- ❌ deploy_failed/timeout/mano_cua_error（+ 原因）
- ⚠️ unclear（+ 说明）

---

## 五、异常处理（Pichai 负责）

| 场景 | 处理 |
|------|------|
| Worker 30 分钟未 ACK | 在 1v1 通道 @Worker 催促 |
| Worker ACK 后 20 分钟无进度 | @Worker 询问状态 |
| Worker 报异常 | 判断可否解决，给建议或标 failed 跳过 |
| Worker 报 deploy_failed | 检查是否 Node 版本问题，建议 nvm 切版本 |
| Worker 完成批次 | Pichai 选下一批卡，写入 dispatch-log |

---

## 六、巡检（Pichai 负责）

当前已配置 cron（`bughunt-trial-patrol`，每 15 分钟），自动检查 Worker 通道活跃度。
超过 20 分钟无进度 → 发告警到主群。

---

## 七、关键注意事项

1. **所有 Worker 汇报消息必须 @Pichai（mention 字段）** — 不带 @ 收不到
2. **dispatch-log 是跨 session 的唯一事实来源** — 所有角色都通过它同步状态
3. **每次操作后都要 push dispatch-log** — git pull → 更新 → git push
4. **每批 5 张** — Worker 完成后再派下一批
5. **同项目同 Worker** — 复用部署是提效关键
6. **Mycroft 发卡必须用 `pool-clean/`** — `pool/` 含 ground_truth，仅供 L2 抽检和 FTY 终审，绝对不发给 Worker
