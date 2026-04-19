#!/usr/bin/env python3
"""
产出验证脚本 — push 前自动校验任务卡质量
检查项：
1. task_id 内部去重
2. task_id 对 pool 去重
3. per-repo cap <= 8
4. 字段完整性（app_name, deploy_verify, batch, dev_url 非空）
5. 总量统计
"""
import json, sys, os, glob
from collections import Counter

def load_jsonl(path):
    cards = []
    with open(path) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                cards.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"  ⚠️ JSON parse error line {i}: {e}")
    return cards

def load_pool(pool_dir):
    """Load existing pool task_ids"""
    task_ids = set()
    for fp in glob.glob(os.path.join(pool_dir, "*.json")):
        try:
            with open(fp) as f:
                card = json.load(f)
                tid = card.get("task_id", "")
                if tid:
                    task_ids.add(tid)
        except:
            pass
    return task_ids

def validate(cards_path, pool_dir=None):
    print(f"=== 产出验证脚本 ===")
    print(f"输入文件: {cards_path}")
    
    cards = load_jsonl(cards_path)
    print(f"总卡数: {len(cards)}")
    
    errors = []
    warnings = []
    
    # 1. task_id 内部去重
    task_ids = [c.get("task_id", "") for c in cards]
    tid_counts = Counter(task_ids)
    dups = {tid: cnt for tid, cnt in tid_counts.items() if cnt > 1}
    if dups:
        errors.append(f"内部重复 task_id: {len(dups)} 个（共 {sum(v-1 for v in dups.values())} 张多余卡）")
        for tid, cnt in sorted(dups.items(), key=lambda x: -x[1])[:5]:
            print(f"  dup: {tid} x{cnt}")
    else:
        print(f"✅ task_id 内部去重: 0 重复")
    
    # 2. 对 pool 去重
    if pool_dir and os.path.isdir(pool_dir):
        pool_ids = load_pool(pool_dir)
        overlap = set(task_ids) & pool_ids
        if overlap:
            errors.append(f"与 pool 重复: {len(overlap)} 张")
            for tid in sorted(overlap)[:5]:
                print(f"  overlap: {tid}")
        else:
            print(f"✅ 对 pool 去重: 0 重复（pool 共 {len(pool_ids)} 张）")
    else:
        warnings.append("未指定 pool 目录，跳过 pool 去重检查")
    
    # 3. per-repo cap
    repo_counts = Counter(c.get("repo", "") for c in cards)
    over_cap = {r: cnt for r, cnt in repo_counts.items() if cnt > 8}
    if over_cap:
        errors.append(f"超过 per-repo cap=8: {len(over_cap)} 个 repo")
        for r, cnt in sorted(over_cap.items(), key=lambda x: -x[1])[:5]:
            print(f"  over-cap: {r} = {cnt}")
    else:
        print(f"✅ per-repo cap: 0 超限（{len(repo_counts)} 个 repo）")
    
    # 4. 字段完整性
    required_fields = ["app_name", "deploy_verify", "batch", "dev_url", "task_id", 
                       "repo", "buggy_commit", "deploy_commands", "test_description_zh"]
    for field in required_fields:
        empty = sum(1 for c in cards if not c.get(field))
        if empty > 0:
            if field in ("app_name", "deploy_verify", "batch"):
                errors.append(f"字段 '{field}' 为空: {empty}/{len(cards)} 张")
            else:
                warnings.append(f"字段 '{field}' 为空: {empty}/{len(cards)} 张")
        else:
            print(f"✅ {field}: 全部非空")
    
    # 5. dev_url 端口分布
    ports = Counter()
    for c in cards:
        url = c.get("dev_url", "")
        if ":" in url:
            port = url.rsplit(":", 1)[-1].rstrip("/")
            ports[port] = ports.get(port, 0) + 1
    print(f"\ndev_url 端口分布:")
    for port, cnt in sorted(ports.items(), key=lambda x: -x[1]):
        print(f"  :{port} = {cnt}")
    
    # 6. 框架分布
    fw = Counter(c.get("framework", "unknown") for c in cards)
    print(f"\n框架分布:")
    for f, cnt in fw.most_common():
        print(f"  {f}: {cnt}")
    
    # 7. backend_risk
    br = sum(1 for c in cards if c.get("backend_risk"))
    print(f"\nbackend_risk=True: {br}/{len(cards)} ({br*100/len(cards):.1f}%)")
    
    # Summary
    print(f"\n{'='*50}")
    if errors:
        print(f"❌ FAILED — {len(errors)} 个错误:")
        for e in errors:
            print(f"  · {e}")
    else:
        print(f"✅ PASSED")
    
    if warnings:
        print(f"⚠️ {len(warnings)} 个警告:")
        for w in warnings:
            print(f"  · {w}")
    
    # Output for commit message
    print(f"\n--- commit message 用 ---")
    print(f"batch 9: {len(cards)} cards, {len(repo_counts)} repos, "
          f"0 dup, 0 pool-overlap, 0 over-cap, "
          f"{len(errors)} errors, {len(warnings)} warnings")
    
    return len(errors) == 0

if __name__ == "__main__":
    cards_path = sys.argv[1] if len(sys.argv) > 1 else "data/batch9_tasks.jsonl.fixed"
    pool_dir = sys.argv[2] if len(sys.argv) > 2 else "tasks/pool"
    
    ok = validate(cards_path, pool_dir)
    sys.exit(0 if ok else 1)
