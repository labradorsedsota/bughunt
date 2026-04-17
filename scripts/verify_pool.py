#!/usr/bin/env python3
"""
BugHunt Pool Verification Script
Checks pool integrity and optionally compares against a batch output file.

Usage:
  python3 scripts/verify_pool.py
  python3 scripts/verify_pool.py --batch-output tasks_batch6.jsonl
  python3 scripts/verify_pool.py --pool-dir /path/to/tasks/pool

Output (always to stdout for commit message embedding):
  VERIFY: +{new} new, ={dup} dup, total={total} cards across {repos} repos
"""

import json, sys, os, argparse
from pathlib import Path
from collections import defaultdict


def main():
    parser = argparse.ArgumentParser(description="BugHunt Pool Verification")
    parser.add_argument("--pool-dir", default="/Users/mlt/.openclaw/workspace/bughunt/tasks/pool",
                        help="Pool directory to verify")
    parser.add_argument("--batch-output", default=None,
                        help="Optional: batch output JSONL file to compare against pool")
    args = parser.parse_args()

    pool_path = Path(args.pool_dir)
    if not pool_path.exists():
        print(f"ERROR: Pool directory does not exist: {args.pool_dir}", file=sys.stderr)
        sys.exit(1)

    # --- Load pool ---
    pool_task_ids = {}  # task_id -> (repo, issue_number)
    pool_repo_issues = set()  # (repo, issue_number) tuples
    errors = []

    for f in sorted(pool_path.glob("*.json")):
        tid = f.stem
        try:
            with open(f) as fh:
                card = json.load(fh)
            repo = card.get("repo", "")
            issue_num = card.get("issue_number", 0)

            # Check for task_id collisions
            if tid in pool_task_ids:
                existing = pool_task_ids[tid]
                if existing[0] != repo:
                    errors.append(f"COLLISION: task_id={tid} maps to both {existing[0]}#{existing[1]} and {repo}#{issue_num}")

            pool_task_ids[tid] = (repo, issue_num)
            if repo and issue_num:
                pool_repo_issues.add((repo, issue_num))
        except Exception as e:
            errors.append(f"READ_ERROR: {f.name}: {e}")

    total_pool = len(pool_task_ids)
    unique_repos = len(set(r for r, _ in pool_task_ids.values()))

    # --- Compare against batch output (optional) ---
    new_count = 0
    dup_count = 0

    if args.batch_output:
        if not os.path.exists(args.batch_output):
            print(f"ERROR: Batch output file does not exist: {args.batch_output}", file=sys.stderr)
            sys.exit(1)

        with open(args.batch_output) as f:
            for line in f:
                try:
                    card = json.loads(line)
                    if card.get("_skipped"):
                        continue
                    tid = card.get("task_id", "")
                    repo = card.get("repo", "")
                    issue_num = card.get("issue_number", 0)

                    is_dup = (tid in pool_task_ids) or ((repo, issue_num) in pool_repo_issues)
                    if is_dup:
                        dup_count += 1
                    else:
                        new_count += 1
                except Exception:
                    continue

    # --- Output ---
    summary = f"VERIFY: +{new_count} new, ={dup_count} dup, total={total_pool} cards across {unique_repos} repos"
    print(summary)

    if errors:
        print(f"\nWARNING: {len(errors)} issues found:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        sys.exit(1)
    else:
        print("CLEAN: no collisions or errors", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
