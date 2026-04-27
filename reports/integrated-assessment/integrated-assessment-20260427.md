# BugHunt Result 整合评估报告

> 生成时间：2026-04-27 14:36  
> 数据源：results/ 全量 1781 张卡 × (合规检查 + 轨迹匹配 + 去重)

---

## 一、综合评级

| 评级 | 含义 | 数量 | 占比 |
|------|------|------|------|
| ✅ A级 | 可交付 | 1267 | 71.1% |
| 🟡 B级 | 有瑕疵 | 39 | 2.2% |
| 🔴 C级 | 需修复 | 393 | 22.1% |
| ⚫ D级 | 无轨迹 | 82 | 4.6% |

---

## 二、result 卡 status 分布

| status | 数量 |
|--------|------|
| completed | 941 |
| failed | 826 |
| deploy_failed | 11 |
| done | 1 |
|  | 1 |
| PARSE_ERROR | 1 |

## 三、mano_cua.status 分布（仅 completed 卡）

| mano_cua.status | 数量 |
|-----------------|------|
| COMPLETED | 662 |
| SKIPPED | 83 |
| STOPPED_BY_USER | 74 |
| ERROR | 29 |
| TIMEOUT | 26 |
| not_started | 15 |
| STOPPED | 14 |
| STOPPED_BY_TIMEOUT | 11 |
| KILLED | 8 |
| HARD_TIMEOUT | 8 |
| NOT_RUN | 8 |
| KILLED_AT_80 | 8 |
| DONE | 6 |
| SIGKILL | 4 |
| FAILED | 3 |
| SKIPPED_SAME_COMMIT | 2 |
| SKIPPED_REPO_FUSE | 2 |
| STOPPED_STEP_LIMIT | 2 |
| NOT_EXECUTED | 2 |
| TERMINATED | 1 |
| KILLED_MAX_STEPS | 1 |
| MAX_STEPS | 1 |

## 四、mano_cua.result 分布

| result | 数量 |
|--------|------|
| abnormal | 378 |
| unclear | 294 |
| normal | 204 |
| deploy_failed | 48 |
| has_bug | 14 |
| reproduced | 8 |
| no_bug | 5 |

## 五、轨迹匹配情况（completed 卡）

| 匹配结果 | 数量 |
|----------|------|
| match | 597 |
| N/A | 280 |
| no_data | 41 |
| mismatch | 20 |
| error | 3 |

## 六、合规性分布

| 合规状态 | 数量 |
|----------|------|
| pass | 1266 |
| fail | 393 |
| warn | 122 |

## 七、C级卡明细（需修复，共 393 张）

| task_id | worker | status | 问题 |
|---------|--------|--------|------|
| apisix-dashboard-3321 | worker-01 | completed | #6, #10 |
| mapbox-gl-draw-1124 | worker-01 | failed | #7, #16 |
| mapbox-gl-draw-571 | worker-01 | failed | #7, #16 |
| mini-qr-219 | worker-01 | completed | #6 |
| open5e-721 | worker-01 | completed | #9 |
| open5e-747 | worker-01 | completed | #9, #10 |
| open5e-803 | worker-01 | completed | #9 |
| Analog-259 | worker-02 | failed | #9 |
| BongoCat-431 | worker-02 | failed | #9 |
| ByteStash-171 | worker-02 | completed | #9 |
| ByteStash-46 | worker-02 | completed | #9 |
| Dante-128 | worker-02 | failed | #9 |
| Piped-3715 | worker-02 | completed | #9 |
| cryptgeon-150 | worker-02 | failed | #9 |
| editable-72 | worker-02 | failed | #2, #7 |
| editable-81 | worker-02 | completed | #6 |
| editable-pr129 | worker-02 | failed | #2, #7 |
| jodit-1335 | worker-02 | done | #3 |
| kan-206 | worker-02 | failed | #9 |
| kan-23 | worker-02 | failed | #9 |
| kan-242 | worker-02 | failed | #9 |
| kan-27 | worker-02 | failed | #9 |
| kan-30 | worker-02 | failed | #9 |
| kirimase-163 | worker-02 | deploy_failed | #2, #3 |
| mavonEditor-649 | worker-02 | completed | #4 |
| mavonEditor-729 | worker-02 | completed | #4 |
| mavonEditor-737 | worker-02 | failed | #7 |
| mavonEditor-pr640 | worker-02 | completed | #4 |
| mavonEditor-pr717 | worker-02 | completed | #4, #6 |
| medium-editor-1047 | worker-02 | completed | #9 |
| mini-media-player-784 | worker-02 | deploy_failed | #2, #3 |
| mint-ui-366 | worker-02 |  | #2, #3 |
| next-redux-wrapper-325 | worker-02 | failed | #9 |
| open5e-622 | worker-02 | completed | #9, #10 |
| open5e-721 | worker-02 | completed | #9 |
| open5e-747 | worker-02 | completed | #9 |
| open5e-803 | worker-02 | completed | #9 |
| org-chart-69 | worker-02 | completed | #9 |
| react-boilerplate-pr2810 | worker-02 | completed | #6 |
| slickgpt-38 | worker-02 | completed | #9 |
| teleport-code-generators-209 | worker-02 | failed | #2, #7 |
| teleport-code-generators-213 | worker-02 | failed | #2, #7 |
| teleport-code-generators-245 | worker-02 | failed | #2, #7 |
| teleport-code-generators-266 | worker-02 | failed | #2, #7 |
| tikzcd-editor-pr5 | worker-02 | completed | #6 |
| twin.macro-528 | worker-02 | failed | #2, #7 |
| twin.macro-576 | worker-02 | failed | #2, #7 |
| twin.macro-pr252 | worker-02 | failed | #2, #7 |
| twin.macro-pr692 | worker-02 | failed | #2, #7 |
| uimix-pr134 | worker-02 | failed | #2, #7 |

*（共 393 张，仅展示前 50 张，完整列表见 CSV）*

## 八、D级卡明细（无轨迹，共 82 张）

| task_id | worker | mano_cua_status |
|---------|--------|-----------------|
| leaflet-geoman-1348 | worker-01 | ERROR |
| svelte-sonner-pr173 | worker-01 | STOPPED_BY_USER |
| the-graph-174 | worker-01 | STOPPED_BY_USER |
| the-graph-pr122 | worker-01 | ERROR |
| jingo-pr189 | worker-02 | STOPPED_BY_TIMEOUT |
| mavonEditor-pr661 | worker-02 | STOPPED_BY_TIMEOUT |
| mission-control-456 | worker-02 | STOPPED_BY_TIMEOUT |
| react-slick-pr2149 | worker-02 | STOPPED_BY_TIMEOUT |
| react-slick-pr622 | worker-02 | STOPPED_BY_TIMEOUT |
| rich-markdown-editor-489 | worker-02 | ERROR |
| gridsheet-pr105 | worker-03 | COMPLETED |
| mui-tiptap-334 | worker-03 | ERROR |
| ngx-scrollbar-674 | worker-03 | COMPLETED |
| coracle-474 | worker-04 | ERROR |
| drawnix-pr318 | worker-04 | STOPPED_BY_USER |
| drawnix-pr333 | worker-04 | STOPPED_BY_USER |
| heynote-195 | worker-04 | STOPPED_BY_USER |
| heynote-357 | worker-04 | TIMEOUT |
| vue-element-plus-admin-316 | worker-04 | HARD_TIMEOUT |
| OpsiMate-408 | worker-05 | STOPPED |
| a11y.css-227 | worker-05 | STOPPED_BY_USER |
| beercss-558 | worker-05 | STOPPED_BY_USER |
| homer-pr112 | worker-05 | TIMEOUT |
| homer-pr115 | worker-05 | TIMEOUT |
| react-dropzone-1449 | worker-05 | STOPPED_BY_USER |
| react-dropzone-526 | worker-05 | STOPPED_BY_USER |
| svelte-typeahead-11 | worker-05 | STOPPED_BY_USER |
| Raneto-88 | worker-06 | STOPPED_BY_USER |
| headscale-ui-pr192 | worker-06 | COMPLETED |
| muya-pr152 | worker-06 | COMPLETED |
| next-themes-85 | worker-06 | STOPPED_BY_USER |
| nuxt-social-share-410 | worker-06 | TIMEOUT |
| pump.io-pr926 | worker-06 | TIMEOUT |
| AlgerMusicPlayer-43 | worker-07 | STOPPED_BY_USER |
| Armoria-pr115 | worker-07 | STOPPED_BY_USER |
| Armoria-pr122 | worker-07 | STOPPED_BY_USER |
| Armoria-pr132 | worker-07 | STOPPED_BY_USER |
| Armoria-pr206 | worker-07 | STOPPED_BY_USER |
| org-chart-290 | worker-07 | COMPLETED |
| reactour-pr405 | worker-07 | STOPPED_BY_USER |
| reactour-pr448 | worker-07 | STOPPED_BY_USER |
| reactour-pr49 | worker-07 | STOPPED_BY_USER |
| reactour-pr529 | worker-07 | STOPPED_BY_USER |
| reactour-pr639 | worker-07 | STOPPED_BY_USER |
| reactour-pr660 | worker-07 | STOPPED_BY_USER |
| svelty-picker-pr156 | worker-07 | STOPPED_BY_USER |
| turnstile-250 | worker-07 | STOPPED_BY_USER |
| visual-drag-demo-pr122 | worker-07 | ERROR |
| visual-drag-demo-pr133 | worker-07 | STOPPED_BY_USER |
| visual-drag-demo-pr27 | worker-07 | STOPPED_BY_USER |
| TiddlyWiki5-9521 | worker-08 | TIMEOUT |
| gitlight-131 | worker-08 | TIMEOUT |
| jsPDF-AutoTable-691 | worker-08 | COMPLETED |
| lumen-300 | worker-08 | TIMEOUT |
| medical-appointment-scheduling-131 | worker-08 | KILLED_AT_80 |
| medical-appointment-scheduling-91 | worker-08 | KILLED_AT_80 |
| ngx-loading-bar-40 | worker-08 | KILLED_AT_80 |
| ngx-loading-bar-43 | worker-08 | KILLED_AT_80 |
| ngx-loading-bar-65 | worker-08 | COMPLETED |
| ngx-loading-bar-85 | worker-08 | COMPLETED |
| nomie6-oss-23 | worker-08 | KILLED_AT_80 |
| openclaw-nerve-140 | worker-08 | TIMEOUT |
| react-timeline-9000-35 | worker-08 | TIMEOUT |
| vue-pdf-98 | worker-08 | TIMEOUT |
| vue-slick-carousel-63 | worker-08 | TIMEOUT |
| air-datepicker-613 | worker-09 | TIMEOUT |
| boardgame.io-782 | worker-09 | COMPLETED |
| boardgame.io-848 | worker-09 | COMPLETED |
| conform-454 | worker-09 | ERROR |
| conform-469 | worker-09 | STOPPED |
| laverna-351 | worker-09 | COMPLETED |
| lenis-68 | worker-09 | TIMEOUT |
| react-datetime-picker-156 | worker-09 | STOPPED |
| react-datetime-picker-40 | worker-09 | STOPPED |
| tracktor-pr139 | worker-09 | TIMEOUT |
| vue-pdf-125 | worker-09 | KILLED |
| vuefinder-pr154 | worker-09 | STOPPED |
| vuetable-2-pr17 | worker-09 | STOPPED |
| ide-9 | worker-fabrice | KILLED |
| media-chrome-697 | worker-fabrice | STOPPED |
| svelte-jsoneditor-pr184 | worker-fabrice | ERROR |
| vuepress-theme-vdoing-pr432 | worker-fabrice | MAX_STEPS |

---

## 九、分 Worker 评级分布

| Worker | A | B | C | D | 总计 |
|--------|---|---|---|---|------|
| worker-01 | 131 | 1 | 7 | 4 | 143 |
| worker-02 | 160 | 9 | 65 | 6 | 240 |
| worker-03 | 169 | 2 | 42 | 3 | 216 |
| worker-04 | 84 | 4 | 77 | 6 | 171 |
| worker-05 | 102 | 6 | 21 | 8 | 137 |
| worker-06 | 130 | 0 | 38 | 6 | 174 |
| worker-07 | 120 | 6 | 22 | 17 | 165 |
| worker-08 | 125 | 0 | 41 | 15 | 181 |
| worker-09 | 174 | 5 | 65 | 13 | 257 |
| worker-fabrice | 72 | 6 | 15 | 4 | 97 |

---

*数据文件：*
- CSV: `reports/integrated-assessment/integrated-assessment-20260427.csv`
- JSON: `reports/integrated-assessment/integrated-assessment-20260427.json`
