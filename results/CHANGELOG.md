# Results CHANGELOG

## 2026-04-17 16:07 — 移除 25 张非标准 schema 结果卡

**操作人：** Pichai（林菡确认）
**原因：** 这 25 张卡的 result JSON 不符合标准 schema（缺少 status 字段、status 值非标准如 deploy_failed/unclear）
**操作：** 从 results/{workerXX}/ 移至 results_archive/trash/，dispatch-log 状态改回 unassigned，后续重新派发

**影响卡列表：**

| # | task_id | 原 Worker | 问题 |
|---|---------|-----------|------|
| 1 | Semantic-UI-React-3864 | worker-02 | missing status field (non-standard schema) |
| 2 | Semantic-UI-React-3994 | worker-02 | missing status field (non-standard schema) |
| 3 | Semantic-UI-React-4005 | worker-02 | missing status field (non-standard schema) |
| 4 | Semantic-UI-React-4083 | worker-02 | missing status field (non-standard schema) |
| 5 | Semantic-UI-React-4110 | worker-02 | missing status field (non-standard schema) |
| 6 | react-content-loader-110 | worker-02 | missing status field (non-standard schema) |
| 7 | emoji-mart-219 | worker-03 | missing status field (non-standard schema) |
| 8 | emoji-mart-220 | worker-03 | missing status field (non-standard schema) |
| 9 | emoji-mart-254 | worker-03 | missing status field (non-standard schema) |
| 10 | emoji-mart-327 | worker-03 | missing status field (non-standard schema) |
| 11 | emoji-mart-762 | worker-03 | missing status field (non-standard schema) |
| 12 | open5e-694 | worker-03 | non-standard status: deploy_failed |
| 13 | open5e-695 | worker-03 | non-standard status: deploy_failed |
| 14 | open5e-716 | worker-03 | non-standard status: deploy_failed |
| 15 | blinko-1068 | worker-09 | non-standard status: deploy_failed |
| 16 | blinko-1138 | worker-09 | non-standard status: deploy_failed |
| 17 | blinko-427 | worker-09 | non-standard status: deploy_failed |
| 18 | blinko-444 | worker-09 | non-standard status: deploy_failed |
| 19 | blinko-802 | worker-09 | non-standard status: deploy_failed |
| 20 | organice-1001 | worker-09 | non-standard status: deploy_failed |
| 21 | organice-1006 | worker-09 | non-standard status: deploy_failed |
| 22 | organice-779 | worker-09 | non-standard status: deploy_failed |
| 23 | organice-784 | worker-09 | non-standard status: deploy_failed |
| 24 | organice-988 | worker-09 | non-standard status: deploy_failed |
| 25 | rich-markdown-editor-489 | worker-09 | non-standard status: unclear |

共 25 张卡。
