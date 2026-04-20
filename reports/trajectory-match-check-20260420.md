# Result卡 vs 轨迹 交叉匹配报告

> 检查时间：2026-04-20 14:35
> 检查范围：所有 completed + 有效 sess_id 的 result 卡

## 一、总览

| 指标 | 数值 |
|------|------|
| 检查总数 | 430 |
| 强匹配通过（app_name + port 双命中）| 216 |
| 语义匹配通过（强匹配 partial + 语义≥阈值）| 186 |
| 弱匹配（部分命中但语义低）| 6 |
| 确认不匹配 | 1 |
| 无本地轨迹 | 21 |
| 无任务卡 | 0 |

## 二、确认不匹配明细（需人工复核）

| task_id | worker | confidence | 共享关键词 |
|---------|--------|------------|------------|
| rich-markdown-editor-447 | worker-01 | 0.037 | cdef, markdown, terminal |

## 三、弱匹配明细（建议人工抽检）

| task_id | worker | confidence | 强匹配情况 | 共享关键词 |
|---------|--------|------------|-----------|------------|
| angular-datepicker-245 | worker-01 | 0.056 | app=✗ port=✓ | date, picker, terminal |
| angular-datepicker-278 | worker-01 | 0.056 | app=✗ port=✓ | datetime, daytimepicker, picker, terminal |
| react-timeline-9000-104 | worker-01 | 0.146 | app=✓ port=✗ | 9000, demo, html, items, react |
| rich-markdown-editor-208 | worker-01 | 0.021 | app=✗ port=✓ | terminal, unclear |
| openclaw-nerve-27 | worker-09 | 0.295 | app=✓ port=✗ | memory, terminal, 一条, 其他, 内容 |
| website-4366 | worker-09 | 0.151 | app=✗ port=✓ | terminal, 始终, 成功, 找到, 某个 |

## 四、无本地轨迹（21 张）

| task_id | sess_id | worker |
|---------|---------|--------|
| apisix-dashboard-3321 | sess-20260419000014-apisix... | worker-01 |
| mini-qr-219 | sess-20260419004700-miniqr... | worker-01 |
| rich-markdown-editor-489 | sess-20260419011513-86383874fe1d48238dd5... | worker-02 |
| svelte-splitpanes-3 | sess-20260419035613-36803f5f043f4e919787... | worker-03 |
| org-chart-215 | sess-20260419033354-7aa0b1657ff04d2d8fa9... | worker-04 |
| a11y.css-227 | sess-20260419002512-d34dbf4195354ec4b781... | worker-05 |
| beercss-558 | sess-20260419011850-d38643db2143437fb64c... | worker-05 |
| svelte-typeahead-11 | sess-20260419022756-48303cd220ad4454b51d... | worker-05 |
| open5e-622 | sess-20260419050517-d506a289b82549b3abd2... | worker-07 |
| org-chart-290 | sess-20260419183322-86feb7ab388f46f4ae57... | worker-07 |
| TiddlyWiki5-9521 | sess-20260419021335-7996e052dfe843018610... | worker-08 |
| gitlight-131 | sess-20260419024629-d428614f070645638b6a... | worker-08 |
| lumen-300 | sess-20260419032013-2dfc5fbbdbdc492d81d1... | worker-08 |
| openclaw-nerve-140 | sess-20260419034556-7d8a612f855a4fdc8ed1... | worker-08 |
| react-timeline-9000-35 | sess-20260419044231-f1db57b319324b5c8f9d... | worker-08 |
| vue-pdf-98 | sess-20260419185256-92e8f1e3b2c74c7cb755... | worker-08 |
| vue-slick-carousel-63 | sess-20260419050424-caa8bf1714524d36b122... | worker-08 |
| Markpad-21 | sess-20260419004624-7b0eef5f3b7a4766becb... | worker-09 |
| vue-pdf-125 | sess-20260419141749-1a20931b03bd42c28c7a... | worker-09 |
| ide-9 | sess-20260419180818-b6eab0fa03284f1489b7... | worker-fabrice |
| media-chrome-697 | sess-20260419061931-140b3d426265483c9285... | worker-fabrice |
