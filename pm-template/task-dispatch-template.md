# 任务派发模板

PM 每次给 Worker 派发任务时，复制以下模板填入实际内容后发送到 1v1 工作通道。

---

## 模板正文

```
📋 第 {N} 批任务（共 {X} 张）

任务列表：
1. {task_id_1}
2. {task_id_2}
3. {task_id_3}
4. {task_id_4}
5. {task_id_5}

执行手册：worker-config/worker-execution-guide.md（repo 里 pull 最新版）
任务卡位置：tasks/pool/ 下对应 JSON 文件
结果输出：results/{worker-XX}/

---

⚠️ 收到后必须做（ACK）：
1. 回复"收到，开始执行第 {N} 批" — 确认你拿到了任务
2. 这条 ACK 必须 @Pichai（带 mention 字段）

⚠️ 执行中必须做（逐 case 上报）：
3. 每完成 1 个 case → @Pichai 发状态信号
   ✅ {task_id} | {耗时} | {判定} | {一句话摘要}
   ❌ {task_id} | {失败类型} | {原因}
   ⚠️ {task_id} | {耗时} | unclear | {说明}
4. 遇异常超 10 分钟解决不了 → 立即 @Pichai 报异常（现象 + 已尝试 + 建议）

⚠️ 全批完成后必须做（闭环）：
5. git push 结果 JSON 到 results/{worker-XX}/
6. @Pichai 报"第 {N} 批完成，{X}✅ {Y}❌ {Z}⚠️，结果已 push，请派下一批"
7. 如果 @Pichai 后 10 分钟无响应，再 @ 一次

⚠️ 所有汇报消息必须 @Pichai（带 mention 字段），否则 PM 收不到。
```

---

## 使用说明

- 每批不超过 5 张卡
- 同项目的卡尽量排在同一批（复用部署）
- 任务卡 JSON 单独发送（一条消息一张卡），不要和指令混在一起
- 发完指令 + 任务卡后，等 Worker ACK 再做其他事

## 变量说明

| 变量 | 含义 | 示例 |
|------|------|------|
| `{N}` | 批次序号 | 1, 2, 3... |
| `{X}` | 本批任务卡数量 | 5 |
| `{task_id}` | 任务卡 ID | medium-editor-1047 |
| `{worker-XX}` | Worker 目录名 | worker-01, worker-fabrice |
| `{耗时}` | case 执行耗时 | 4m32s |
| `{判定}` | abnormal / normal / unclear | abnormal |
| `{失败类型}` | deploy_failed / timeout / mano_cua_error / other | deploy_failed |
