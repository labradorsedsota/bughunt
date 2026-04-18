#!/usr/bin/env python3
"""Fix worker-08 non-compliant result files: completed+SKIPPED → failed template"""
import json
import os

RESULTS_DIR = "/Users/worker08/bughunt/results/worker-08"

# All files needing fix: original 31 from audit + 4 from batch 8
SKIPPED_FILES = [
    "Task-Board-516", "clappr-1868", "devtools-768", "elements-936", "epicenter-1637",
    "freespeech-21", "frontend-3712", "gitlight-56", "hls-downloader-491", "kan-320",
    "karakeep-2511", "karakeep-2569", "karakeep-2640", "lms-1583", "marble-296",
    "minimal-chat-99", "misskey-hub-next-101", "plot-2274", "rawgraphs-app-113",
    "react-design-editor-244", "react-native-web-2794", "react-pdf-1530", "shopify-261",
    "sorry-cypress-228", "sorry-cypress-392", "sorry-cypress-849", "static-cms-790",
    "suneditor-1205", "tui.editor-1806", "website-v2-1887", "win11React-658",
    # batch 8 additions
    "gitlight-222", "meilisearch-ui-239", "bobarr-57", "useSend-177"
]

# Manually curated attempted lists based on actual work done
ATTEMPTED_MAP = {
    # Network failures - tried proxy + direct + shallow clone
    "freespeech-21": ["代理 clone（超时）", "直连 clone（github.com 不通）", "shallow clone + fetch --unshallow（失败）"],
    "karakeep-2511": ["代理 clone（76MB 超时）", "直连 clone（不通）"],
    "karakeep-2569": ["代理 clone（76MB 超时）", "直连 clone（不通）"],
    "karakeep-2640": ["代理 clone（76MB 超时）", "直连 clone（不通）"],
    "marble-296": ["代理 clone（90MB 超时）", "直连 clone（不通）"],
    "minimal-chat-99": ["代理 clone（61MB 超时）", "直连 clone（不通）"],
    "misskey-hub-next-101": ["代理 clone（75MB 超时）", "直连 clone（不通）"],
    "plot-2274": ["代理 clone（95MB 超时）", "直连 clone（不通）"],
    "react-design-editor-244": ["代理 clone（60MB 超时）", "直连 clone（不通）"],
    "react-native-web-2794": ["代理 clone（93MB 超时）", "直连 clone（不通）"],
    "static-cms-790": ["代理 clone（86MB 超时）", "直连 clone（不通）"],
    "suneditor-1205": ["代理 clone（75MB 超时）", "直连 clone（不通）"],
    "tui.editor-1806": ["代理 clone（80MB 超时）", "直连 clone（不通）"],
    "website-v2-1887": ["代理 clone（91MB 超时）", "直连 clone（不通）"],
    "win11React-658": ["代理 clone（91MB 超时）", "直连 clone（不通）"],
    "meilisearch-ui-239": ["代理 clone（超时）", "直连 clone（不通）", "shallow clone + fetch（pack 文件损坏）"],
    # Deploy failures - tried various approaches
    "clappr-1868": ["npm install --legacy-peer-deps（node-sass arm64 编译失败）", "npm rebuild node-sass（同一错误）"],
    "devtools-768": ["pnpm install（成功）", "pnpm dev:prepare（Cannot find module uno.config）"],
    "elements-936": ["npm install（成功）", "turbo dev（类型错误导致 build 失败）"],
    "epicenter-1637": ["npm install（EUNSUPPORTEDPROTOCOL catalog: 协议不支持）"],
    "frontend-3712": ["yarn install（两次超时被 kill）", "npm install --legacy-peer-deps（缺 workspace 包）", "rsbuild dev（4 个 Module not found 错误）"],
    "rawgraphs-app-113": ["检查项目结构（无 package.json，需 bower）"],
    "react-pdf-1530": ["npm install（portal: 协议不支持）", "yarn 3 install（超时）"],
    # Not web apps
    "Task-Board-516": [],
    "hls-downloader-491": [],
    # Backend required - identified quickly, no deploy attempted
    "gitlight-56": ["clone 成功", "检查 .env（需 AUTH_GITHUB_ID/SECRET/AUTH_SECRET）"],
    "gitlight-222": ["复用 gitlight clone", "检查 .env（同 gitlight-56，需 OAuth）"],
    "kan-320": ["clone 成功", "npm install（成功）", "npm run dev（next.config.js 加载失败，缺 BETTER_AUTH_SECRET）"],
    "lms-1583": ["代理 clone（100MB 超时）"],
    "shopify-261": ["clone 成功", "检查 .env（需 SHOPIFY_STOREFRONT_TOKEN）"],
    "sorry-cypress-228": ["clone 成功", "检查项目结构（需 MongoDB + Director/API 后端）"],
    "sorry-cypress-392": ["clone 成功", "检查项目结构（需 MongoDB + Director/API 后端）"],
    "sorry-cypress-849": ["clone 成功", "检查项目结构（需 MongoDB + Director/API 后端）"],
    "bobarr-57": ["代理 clone（超时）"],
    "useSend-177": ["代理 clone 成功", "检查 .env（需 PostgreSQL + Redis + SMTP + NextAuth）"],
}

# Recommendations
RECOMMENDATION_MAP = {
    # Network
    "freespeech-21": "需稳定网络环境或本地镜像",
    "karakeep-2511": "需稳定网络环境（76MB repo）",
    "karakeep-2569": "需稳定网络环境（76MB repo）",
    "karakeep-2640": "需稳定网络环境（76MB repo）",
    "marble-296": "需稳定网络环境（90MB repo）",
    "minimal-chat-99": "需稳定网络环境（61MB repo）",
    "misskey-hub-next-101": "需稳定网络环境（75MB repo）",
    "plot-2274": "需稳定网络环境（95MB repo）",
    "react-design-editor-244": "需稳定网络环境（60MB repo）",
    "react-native-web-2794": "需稳定网络环境（93MB repo）",
    "static-cms-790": "需稳定网络环境（86MB repo）",
    "suneditor-1205": "需稳定网络环境（75MB repo）",
    "tui.editor-1806": "需稳定网络环境（80MB repo）",
    "website-v2-1887": "需稳定网络环境（91MB repo）",
    "win11React-658": "需稳定网络环境（91MB repo）",
    "meilisearch-ui-239": "需稳定网络 + Meilisearch 后端",
    # Deploy
    "clappr-1868": "需 Node 14 + x86 环境（node-sass 不支持 arm64）",
    "devtools-768": "Nuxt DevTools monorepo 内部依赖问题，跳过",
    "elements-936": "monorepo 类型错误，跳过",
    "epicenter-1637": "需安装 bun@1.3.3",
    "frontend-3712": "需 yarn 4 + 稳定网络",
    "rawgraphs-app-113": "旧版 bower 项目，需 bower install",
    "react-pdf-1530": "需 yarn 3 workspace 环境",
    # Not web apps
    "Task-Board-516": "Obsidian 插件，无法浏览器测试",
    "hls-downloader-491": "Chrome 扩展，无法 localhost 测试",
    # Backend
    "gitlight-56": "需 GitHub OAuth 凭证",
    "gitlight-222": "需 GitHub/GitLab OAuth 凭证",
    "kan-320": "需 BETTER_AUTH_SECRET 等环境变量",
    "lms-1583": "需 Frappe 框架后端（Python + MariaDB）",
    "shopify-261": "需 Shopify Storefront API 凭证",
    "sorry-cypress-228": "需 MongoDB + Director/API 后端",
    "sorry-cypress-392": "需 MongoDB + Director/API 后端",
    "sorry-cypress-849": "需 MongoDB + Director/API 后端",
    "bobarr-57": "需 Docker Compose 多后端（PostgreSQL/Redis/Jackett/qBittorrent）",
    "useSend-177": "需 PostgreSQL + Redis + SMTP + NextAuth",
}

fixed = 0
for fname in SKIPPED_FILES:
    path = os.path.join(RESULTS_DIR, f"{fname}.json")
    with open(path) as f:
        old = json.load(f)
    
    # Extract symptom from old result_summary
    symptom = ""
    if old.get("mano_cua") and old["mano_cua"].get("result_summary"):
        symptom = old["mano_cua"]["result_summary"]
    
    attempted = ATTEMPTED_MAP.get(fname, [])
    recommendation = RECOMMENDATION_MAP.get(fname, "跳过")
    
    new = {
        "task_id": old["task_id"],
        "repo": old["repo"],
        "worker": old["worker"],
        "status": "failed",
        "sess_id": None,
        "expected_result_used": False,
        "duration_seconds": old.get("duration_seconds", 0),
        "timestamp": old.get("timestamp", ""),
        "mano_cua": None,
        "failure": {
            "type": "deploy_failed",
            "symptom": symptom,
            "attempted": attempted,
            "recommendation": recommendation
        }
    }
    
    with open(path, 'w') as f:
        json.dump(new, f, indent=2, ensure_ascii=False)
    
    fixed += 1
    print(f"✅ {fname}")

print(f"\n共修复 {fixed} 张卡")
EOF