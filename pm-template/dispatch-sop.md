# 派发工作 SOP（交接文档）

> 本文档描述 PM 派发任务给 Worker 的完整工作方法。接手人读完此文档即可独立执行派发工作。

---

## 一、整体流程

```
选卡 → 发派发消息 → 等 ACK → 收状态信号 → 更新 dispatch-log → 批次完成后派下一批
```

---

## 二、选卡规则

### 2.1 数据来源

- 任务卡池：`tasks/pool/` 目录下的 JSON 文件（当前 727 张）
- 已派发记录：`pm-template/dispatch-log.md`（唯一事实来源）

### 2.2 选卡原则

1. **不重复派发** — 先读 dispatch-log.md，跳过已派发的 task_id
2. **纯净卡优先** — 优先选 `backend_risk` 为 false 或不存在的卡
3. **同项目同 Worker** — 同一个项目（repo）的多张卡分给同一个 Worker，共享 clone + install，只换 buggy_commit
4. **每批 5 张** — 每次派发 5 张卡为一批
5. **均匀分配** — 多个 Worker 同时派发时，每个 Worker 的卡数尽量相等

### 2.3 选卡脚本参考

```python
import json, os
from collections import defaultdict

# 读取已派发的 task_id（从 dispatch-log.md 解析，或维护一个 set）
already_assigned = set()  # 填入已派发的 task_id

# 读取所有卡
pool_dir = 'tasks/pool'
cards = []
for f in sorted(os.listdir(pool_dir)):
    if f.endswith('.json'):
        with open(os.path.join(pool_dir, f)) as fh:
            card = json.load(fh)
        if card['task_id'] not in already_assigned and not card.get('backend_risk', False):
            cards.append(card)

# 按项目分组
by_project = defaultdict(list)
for c in cards:
    proj = c.get('repo', '').split('/')[-1]
    by_project[proj].append(c)

# 按项目卡数降序排，优先分配多卡项目（复用部署收益大）
sorted_projects = sorted(by_project.items(), key=lambda x: -len(x[1]))
```

---

## 三、派发消息

### 3.1 Worker 1v1 通道

每个 Worker 有专属的 1v1 工作通道，**所有任务派发只通过 1v1 通道发送**。

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

### 3.2 发送顺序（每个 Worker）

**第 1 条：派发指令**（必须 @Worker）

```
@{worker名} 📋 第 {N} 批任务（共 {X} 张）

任务列表：
1. {task_id_1}
2. {task_id_2}
...

执行手册：worker-config/worker-execution-guide.md（repo 里 pull 最新版）
任务卡位置：tasks/pool/ 下对应 JSON 文件
结果输出：results/{worker-XX}/

同项目多张卡共享 clone + install，只需切换 buggy_commit。
```

发送时 payload 必须带 mention 字段：
```json
{"mention": {"uids": ["{worker_uid}"]}}
```

**第 2 条：汇报规则**

```
⚠️ 汇报规则（必须遵守）：

1. 收到任务 → @Pichai 回复"收到，开始执行第 {N} 批"
2. 每完成 1 个 case → @Pichai 发状态（✅/❌/⚠️ task_id | 耗时 | 判定 | 摘要）
3. 遇异常超 10 分钟解决不了 → @Pichai 报异常
4. 全批完成 → @Pichai 报"第 {N} 批完成，X✅ Y❌ Z⚠️，结果已 push，请派下一批"
5. ⚠️ 每个 case 完成 mano-cua 后，先发状态信号再开始下一个 case，不要一口气跑完再汇报
6. 所有汇报消息必须 @Pichai（带 mention 字段），否则我收不到

现在请先 @Pichai 回复 ACK。
```

**第 3-7 条：逐张发任务卡 JSON**

每张卡单独一条消息，格式：
```
📄 任务卡 {序号}/{总数}: {task_id}

{完整 JSON 内容}
```

### 3.3 发送 API

```bash
curl -s -X POST "https://im.deepminer.com.cn/api/v1/bot/sendMessage" \
  -H "Authorization: Bearer {BOT_TOKEN}" \
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

- BOT_TOKEN: `bf_f44080a9a3d4b527b2ab93c42dc9571c`（Pichai 的 bot token）
- channel_type 固定为 2（群聊）
- mention 字段只在第 1 条（@Worker）时需要，后续消息可不带

### 3.4 消息间隔

每条消息之间间隔 200-300ms，避免消息乱序。

---

## 四、更新 dispatch-log

**每次派发后必须更新 `pm-template/dispatch-log.md` 并 push 到 repo。**

### 4.1 更新内容

1. **当前状态总览表** — 新增一行或更新已有行
2. **派发记录** — 追加一条新记录

### 4.2 记录格式

```markdown
### [时间] 第 N 批 → worker-XX

**状态：** 已派发，等待 ACK

**任务列表：**
1. task_id_1 — 🔲 待执行
2. task_id_2 — 🔲 待执行
...

**进度：** 0/5 完成
**备注：** 同项目 xxx，共享部署
```

### 4.3 状态流转

```
已派发，等待 ACK → ACK已确认，执行中 → 已完成
```

每个 task_id 的状态标记：
- 🔲 待执行
- ⏳ 执行中
- ✅ abnormal/normal（+ 耗时 + 摘要）
- ❌ deploy_failed/timeout/mano_cua_error（+ 原因）
- ⚠️ unclear（+ 说明）

### 4.4 收到 Worker 状态信号时

Worker @Pichai 发状态信号后，更新 dispatch-log 中对应 task_id 的状态，push。

### 4.5 批次完成时

Worker 报"第 N 批完成"后：
1. 更新该记录状态为"已完成"
2. 把该记录移到历史记录区
3. 如果还有未派发的卡，准备下一批并派发

---

## 五、异常处理

| 场景 | 处理 |
|------|------|
| Worker 30 分钟未 ACK | 在 1v1 通道 @Worker 催促，确认是否在线 |
| Worker ACK 后 20 分钟无进度 | @Worker 询问当前状态 |
| Worker 报异常 | 判断是否可解决：可解决给建议，不可解决标 failed 跳过 |
| Worker 报 deploy_failed | 检查是否 Node 版本问题，建议 nvm 切版本 |
| Worker 完成批次后 PM 10 分钟内没派下一批 | Worker 会再 @ 一次，收到后立即派发 |

---

## 六、巡检 cron

当前已配置巡检 cron（`bughunt-trial-patrol`，每 15 分钟），自动检查 Worker 通道活跃度。

巡检逻辑：
- 读取各 Worker 1v1 通道的最近消息
- 超过 20 分钟无进度 → 发告警到主群
- 巡检报告发到「从github找CUA数据」主群

---

## 七、关键注意事项

1. **所有消息必须带 @（mention 字段）** — 不带 @ 的消息对方收不到，这是之前试跑暴露的核心问题
2. **dispatch-log 是唯一事实来源** — 不同 session 之间不共享上下文，必须通过 dispatch-log 同步状态
3. **每次操作后都要 push dispatch-log** — git pull → 更新 → git push，保持在线可查
4. **不要一次性派发太多** — 每批 5 张，Worker 完成后再派下一批
5. **同项目同 Worker** — 复用部署是提效的关键
