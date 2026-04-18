#!/usr/bin/env python3
"""Fix 29 non-compliant worker-09 result files per approved plan."""
import json
import os
import re
from datetime import datetime

RESULTS_DIR = "/Users/worker09/.openclaw/workspace/bughunt/results/worker-09"
LOGS_DIR = "/Users/worker09/.openclaw/workspace/bughunt/logs"
WORKER = "worker-09"
NOW = "2026-04-17T20:30:00-07:00"

def read_json(path):
    with open(path) as f:
        return json.load(f)

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ✅ wrote {os.path.basename(path)}")

def extract_last_reasoning(log_file):
    """Extract full last_reasoning text from log file."""
    path = os.path.join(LOGS_DIR, log_file)
    if not os.path.exists(path):
        return None
    with open(path) as f:
        content = f.read()
    m = re.search(r'Last reasoning: (.+?)(?:\n={10,}|\Z)', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return None

def make_completed(task_id, repo, sess_id, expected_result_used, duration_seconds,
                   timestamp, mano_status, total_steps, last_action, result,
                   result_summary, last_reasoning):
    return {
        "task_id": task_id,
        "repo": repo,
        "worker": WORKER,
        "status": "completed",
        "sess_id": sess_id,
        "expected_result_used": expected_result_used,
        "duration_seconds": duration_seconds,
        "timestamp": timestamp,
        "mano_cua": {
            "status": mano_status,
            "total_steps": total_steps,
            "last_action": last_action,
            "result": result,
            "result_summary": result_summary,
            "last_reasoning": last_reasoning
        }
    }

def make_failed(task_id, repo, timestamp, failure_type, symptom, attempted, recommendation):
    return {
        "task_id": task_id,
        "repo": repo,
        "worker": WORKER,
        "status": "failed",
        "expected_result_used": False,
        "sess_id": None,
        "duration_seconds": 0,
        "timestamp": timestamp,
        "mano_cua": None,
        "failure": {
            "type": failure_type,
            "symptom": symptom,
            "attempted": attempted,
            "recommendation": recommendation
        }
    }

def fix_all():
    fixed = []

    # ==================== TYPE A: 3 COMPLETED ====================
    print("\n=== Type A: Completed (3 files) ===")

    # 1. openclaw-nerve-27
    orig = read_json(os.path.join(RESULTS_DIR, "openclaw-nerve-27.json"))
    lr = extract_last_reasoning("openclaw-nerve-27-v3.log")
    data = make_completed(
        task_id="openclaw-nerve-27",
        repo=orig["repo"],
        sess_id="sess-20260417152916-7a76ffb7d5dc4402b0c0dee4494e2fa2",
        expected_result_used=False,
        duration_seconds=1500,  # ~25 min across 3 sessions
        timestamp="2026-04-17T00:33:00-07:00",
        mano_status="COMPLETED",
        total_steps=25,
        last_action="DONE",
        result="abnormal",
        result_summary="Memory API routes validate filenames with date regex, rejecting non-date entries like project-notes. All memory list items unresponsive when clicked.",
        last_reasoning=lr or orig.get("reasoning", "")
    )
    write_json(os.path.join(RESULTS_DIR, "openclaw-nerve-27.json"), data)
    fixed.append(("openclaw-nerve-27", "status=None, 缺必填字段, 旧格式", "completed", "从 log 提取 last_action=DONE/last_reasoning; sess_id 取最后 COMPLETED session"))

    # 2. shadcn-solid-77
    orig = read_json(os.path.join(RESULTS_DIR, "shadcn-solid-77.json"))
    lr = extract_last_reasoning("shadcn-solid-77.log")
    data = make_completed(
        task_id="shadcn-solid-77",
        repo=orig["repo"],
        sess_id="sess-20260417162649-55b46acf5a944bf2a1a88114684ecd39",
        expected_result_used=False,
        duration_seconds=600,
        timestamp="2026-04-17T01:32:00-07:00",
        mano_status="COMPLETED",
        total_steps=26,
        last_action="DONE",
        result="abnormal",
        result_summary="Astro logo completely invisible in light mode (white SVG on white background). Dark mode shows logo clearly.",
        last_reasoning=lr or orig.get("reasoning", "")
    )
    write_json(os.path.join(RESULTS_DIR, "shadcn-solid-77.json"), data)
    fixed.append(("shadcn-solid-77", "status=None, 缺必填字段, 旧格式", "completed", "从 log 提取 last_action=DONE/last_reasoning; mano-cua COMPLETED 26步"))

    # 3. shadcn-solid-122
    orig = read_json(os.path.join(RESULTS_DIR, "shadcn-solid-122.json"))
    lr = extract_last_reasoning("shadcn-solid-122.log")
    data = make_completed(
        task_id="shadcn-solid-122",
        repo=orig["repo"],
        sess_id="sess-20260417164307-75086a9d412f4a8da5e7c1bdea683d6e",
        expected_result_used=False,
        duration_seconds=180,
        timestamp="2026-04-17T01:44:00-07:00",
        mano_status="COMPLETED",
        total_steps=6,
        last_action="DONE",
        result="abnormal",
        result_summary="Examples section empty — Checkboxes and Radio Group headings only, no demo components or code snippets. Code snippet / Demo reference mismatch confirmed via source.",
        last_reasoning=lr or orig.get("reasoning", "")
    )
    write_json(os.path.join(RESULTS_DIR, "shadcn-solid-122.json"), data)
    fixed.append(("shadcn-solid-122", "status=None, 缺必填字段, 旧格式", "completed", "从 log 提取 last_action=DONE/last_reasoning; mano-cua COMPLETED 6步"))

    # ==================== TYPE A: 4 FAILED ====================
    print("\n=== Type A: Failed (4 files) ===")

    # 4. Luckysheet-528
    orig = read_json(os.path.join(RESULTS_DIR, "Luckysheet-528.json"))
    data = make_failed(
        task_id="Luckysheet-528",
        repo=orig["repo"],
        timestamp="2026-04-17T03:06:00-07:00",
        failure_type="mano_cua_error",
        symptom="mano-cua 72步后被 SIGKILL，无法定位 Luckysheet 条件格式对话框入口。Bug 通过源码分析确认：Data Bar 条件格式对字符串单元格 valueLen=NaN 未校验，canvas 绘制崩溃。",
        attempted=["mano-cua 执行 72 步尝试定位条件格式功能入口"],
        recommendation="deploy_failed 但源码确认 bug 存在：valueLen=NaN 未校验导致 canvas 崩溃"
    )
    write_json(os.path.join(RESULTS_DIR, "Luckysheet-528.json"), data)
    fixed.append(("Luckysheet-528", "status=None, 缺必填字段, 旧格式", "failed (mano_cua_error)", "72步 SIGKILL→failed; 源码分析保留在 symptom/recommendation"))

    # 5. Starkiller-5
    orig = read_json(os.path.join(RESULTS_DIR, "Starkiller-5.json"))
    data = make_failed(
        task_id="Starkiller-5",
        repo=orig["repo"],
        timestamp="2026-04-17T03:30:00-07:00",
        failure_type="deploy_failed",
        symptom="Starkiller 需要 Empire C2 后端登录，无法纯前端测试。Bug 通过源码分析确认：createListener API 硬编码 /listeners/http，非 HTTP 类型必报 400。",
        attempted=[],
        recommendation="deploy_failed 但源码确认 bug 存在：createListener 硬编码 /listeners/http"
    )
    write_json(os.path.join(RESULTS_DIR, "Starkiller-5.json"), data)
    fixed.append(("Starkiller-5", "status=None, 缺必填字段, 旧格式", "failed (deploy_failed)", "需 Empire C2 后端; 源码分析保留在 recommendation"))

    # 6. Task-Board-608
    orig = read_json(os.path.join(RESULTS_DIR, "Task-Board-608.json"))
    data = make_failed(
        task_id="Task-Board-608",
        repo=orig["repo"],
        timestamp="2026-04-17T03:33:00-07:00",
        failure_type="deploy_failed",
        symptom="Obsidian 插件，无法独立浏览器运行。Bug 通过源码分析确认：sidebar board list 缺 overflow-y:scroll 和 max-height，多 board 溢出不可滚动。",
        attempted=[],
        recommendation="deploy_failed 但源码确认 bug 存在：sidebar 缺 overflow-y:scroll"
    )
    write_json(os.path.join(RESULTS_DIR, "Task-Board-608.json"), data)
    fixed.append(("Task-Board-608", "status=None, 缺必填字段, 旧格式", "failed (deploy_failed)", "Obsidian 插件无法浏览器运行; 源码分析保留在 recommendation"))

    # 7. openclaw-nerve-64
    orig = read_json(os.path.join(RESULTS_DIR, "openclaw-nerve-64.json"))
    data = make_failed(
        task_id="openclaw-nerve-64",
        repo=orig["repo"],
        timestamp="2026-04-17T00:53:00-07:00",
        failure_type="deploy_failed",
        symptom="STT 后端不可用，用户主动停止（48 步）。Bug 通过源码分析确认：Chat 面板条件渲染卸载 voice 状态，切换面板后录音丢失。",
        attempted=["mano-cua 执行 48 步，尝试通过键盘快捷键触发语音录制"],
        recommendation="deploy_failed 但源码确认 bug 存在：条件渲染导致 voice 状态卸载"
    )
    write_json(os.path.join(RESULTS_DIR, "openclaw-nerve-64.json"), data)
    fixed.append(("openclaw-nerve-64", "status=None, 缺必填字段, 旧格式", "failed (deploy_failed)", "STT 后端不可用→deploy_failed; 源码分析保留在 recommendation"))

    # ==================== TYPE B: 16 FAILED ====================
    print("\n=== Type B: Failed format fix (16 files) ===")

    # kaneo series (5)
    kaneo_ids = ["kaneo-1066", "kaneo-1081", "kaneo-1087", "kaneo-1131", "kaneo-1140"]
    for tid in kaneo_ids:
        orig = read_json(os.path.join(RESULTS_DIR, f"{tid}.json"))
        data = make_failed(
            task_id=tid,
            repo=orig["repo"],
            timestamp=orig.get("timestamp", NOW),
            failure_type="deploy_failed",
            symptom=orig.get("notes", "需要 PostgreSQL 数据库，本机未安装，API ECONNREFUSED"),
            attempted=[],
            recommendation="跳过，需 PostgreSQL"
        )
        write_json(os.path.join(RESULTS_DIR, f"{tid}.json"), data)
        fixed.append((tid, "failure=null, 缺 sess_id/expected_result_used/duration_seconds", "failed (deploy_failed)", "failure_reason/notes→标准 failure 对象; 补缺失字段"))

    # megadraft series (6)
    mega_ids = ["megadraft-283", "megadraft-286", "megadraft-288", "megadraft-302", "megadraft-319", "megadraft-324"]
    for tid in mega_ids:
        orig = read_json(os.path.join(RESULTS_DIR, f"{tid}.json"))
        data = make_failed(
            task_id=tid,
            repo=orig["repo"],
            timestamp=orig.get("timestamp", NOW),
            failure_type="deploy_failed",
            symptom=orig.get("error_detail", "node-sass 不支持 Apple Silicon arm64 + Node 23"),
            attempted=[],
            recommendation="跳过，node-sass 不支持 arm64 + Node 23"
        )
        write_json(os.path.join(RESULTS_DIR, f"{tid}.json"), data)
        fixed.append((tid, "failure=null, 缺 sess_id/expected_result_used/duration_seconds", "failed (deploy_failed)", "reason/error_detail→标准 failure 对象; 补缺失字段"))

    # react-hot-toast series (5)
    rht_ids = ["react-hot-toast-10", "react-hot-toast-27", "react-hot-toast-45", "react-hot-toast-50", "react-hot-toast-101"]
    for tid in rht_ids:
        orig = read_json(os.path.join(RESULTS_DIR, f"{tid}.json"))
        data = make_failed(
            task_id=tid,
            repo=orig["repo"],
            timestamp=orig.get("timestamp", NOW),
            failure_type="deploy_failed",
            symptom=orig.get("error_detail", "pnpm install prepare 脚本 tsdx build 失败，@babel/parser 不支持 TypeScript export type 语法"),
            attempted=[],
            recommendation="跳过，tsdx build 不兼容当前环境"
        )
        write_json(os.path.join(RESULTS_DIR, f"{tid}.json"), data)
        fixed.append((tid, "failure=null, 缺 sess_id/expected_result_used/duration_seconds", "failed (deploy_failed)", "reason/error_detail→标准 failure 对象; 补缺失字段"))

    # ==================== TYPE C: 6 FAILED (completed→failed) ====================
    print("\n=== Type C: completed→failed (6 files) ===")

    type_c = [
        ("devtools-598", "checkForUpdateOf 缺 modulesDir，monorepo 下版本不显示"),
        ("maker.js-556", "tryAddCaption 缺 m.origin 偏移，嵌套模型 caption 位置错误"),
        ("ngx-datatable-1702", "@ViewChild static:true 应为 false，scroller 未解析导致虚拟分页失效"),
        ("ngx-page-scroll-2", "EventEmitter 缺泛型参数导致 async 模式，router outlet 内事件不触发"),
        ("react-grid-layout-918", "calcXY 用 margin 而非 containerPadding 偏移，placeholder 位置错误"),
        ("shikwasa-44", ".shk-icons 单例共享，销毁一个播放器导致其他实例 SVG 图标消失"),
    ]

    for tid, bug_desc in type_c:
        orig = read_json(os.path.join(RESULTS_DIR, f"{tid}.json"))
        # Extract symptom from original mano_cua result_summary if available
        orig_mano = orig.get("mano_cua", {}) or {}
        orig_summary = orig_mano.get("result_summary", "")
        symptom = orig_summary if orig_summary else f"部署失败，mano-cua 未执行。源码分析确认 bug：{bug_desc}"

        data = make_failed(
            task_id=tid,
            repo=orig["repo"],
            timestamp=orig.get("timestamp", NOW),
            failure_type="deploy_failed",
            symptom=symptom if len(symptom) < 200 else symptom[:200],
            attempted=["Source code analysis"],
            recommendation=f"deploy_failed 但源码确认 bug 存在：{bug_desc}"
        )
        write_json(os.path.join(RESULTS_DIR, f"{tid}.json"), data)
        fixed.append((tid, "sess_id=null (completed 但 mano-cua 未执行)", "failed (deploy_failed)", "completed→failed; 源码分析保留在 recommendation"))

    # ==================== SUMMARY ====================
    print(f"\n{'='*60}")
    print(f"Total files fixed: {len(fixed)}")
    print(f"  Completed: 3")
    print(f"  Failed: {len(fixed) - 3}")

    return fixed

if __name__ == "__main__":
    fixed = fix_all()
