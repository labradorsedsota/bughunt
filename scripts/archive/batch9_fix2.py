#!/usr/bin/env python3
"""
Batch 9 第二轮修复：补 app_name / deploy_verify / batch / Vue老项目端口
输入: data/batch9_tasks.jsonl.fixed
输出: data/batch9_tasks.jsonl.fixed2
"""
import json, re

# Vue CLI 老项目列表（用 Vue CLI / webpack，端口 8080 而非 5173）
VUE_CLI_REPOS = {
    "iview", "view-design", "vux", "nutui", "element-ui", "element-plus",
    "vue-element-admin", "vant", "mint-ui", "muse-ui", "vuetify",
    "buefy", "bootstrap-vue", "vue-material", "keen-ui", "at-ui",
    "cube-ui", "vue-beauty", "vue-admin", "d2-admin", "vue-manage-system"
}

def repo_to_app_name(repo):
    """从 repo 名生成 app_name: 'user/json-crack' -> 'JSON Crack'"""
    name = repo.split("/")[-1] if "/" in repo else repo
    # 去掉常见后缀
    for suffix in [".com", ".io", ".org", ".js", ".ts", "-app", "-ui"]:
        if name.lower().endswith(suffix):
            name = name[:-len(suffix)]
    # 连字符/下划线转空格，首字母大写
    name = re.sub(r"[-_]+", " ", name)
    # 智能大写：保留全大写缩写，其他 title case
    words = name.split()
    result = []
    for w in words:
        if w.upper() == w and len(w) <= 5:
            result.append(w.upper())
        else:
            result.append(w.capitalize())
    return " ".join(result)

def make_deploy_verify(dev_url):
    """从 dev_url 生成 deploy_verify 命令"""
    return f"curl -s {dev_url} | grep -q '<'"

def is_vue_cli_project(card):
    """判断是否是 Vue CLI 老项目"""
    repo = card.get("repo", "")
    repo_name = repo.split("/")[-1].lower() if "/" in repo else repo.lower()
    # 精确匹配已知 Vue CLI 项目
    for known in VUE_CLI_REPOS:
        if known.lower() in repo_name:
            return True
    # 检查 deploy_commands 是否含 vue-cli-service 或 webpack
    cmds = card.get("deploy_commands", "")
    if "vue-cli-service" in cmds or "webpack-dev-server" in cmds:
        return True
    return False

INPUT = "/tmp/bughunt-sophon/data/batch9_tasks.jsonl.fixed"
OUTPUT = "/tmp/bughunt-sophon/data/batch9_tasks.jsonl.fixed2"

cards = []
vue_port_fixes = 0

with open(INPUT) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        card = json.loads(line)
        
        # 1. 补 app_name
        card["app_name"] = repo_to_app_name(card.get("repo", ""))
        
        # 2. 补 deploy_verify
        card["deploy_verify"] = make_deploy_verify(card.get("dev_url", "http://localhost:5173"))
        
        # 3. 补 batch
        card["batch"] = 9
        
        # 4. Vue 老项目端口修正 (5173 -> 8080)
        if card.get("framework") == "vue" and is_vue_cli_project(card):
            old_url = card.get("dev_url", "")
            if ":5173" in old_url:
                card["dev_url"] = old_url.replace(":5173", ":8080")
                card["deploy_verify"] = make_deploy_verify(card["dev_url"])
                # 同步修正 deploy_commands
                if "5173" in card.get("deploy_commands", ""):
                    card["deploy_commands"] = card["deploy_commands"].replace("5173", "8080")
                vue_port_fixes += 1
        
        cards.append(card)

with open(OUTPUT, "w") as f:
    for card in cards:
        f.write(json.dumps(card, ensure_ascii=False) + "\n")

print(f"修复完成:")
print(f"  总卡数: {len(cards)}")
print(f"  app_name 补充: {sum(1 for c in cards if c.get('app_name'))}/{len(cards)}")
print(f"  deploy_verify 补充: {sum(1 for c in cards if c.get('deploy_verify'))}/{len(cards)}")
print(f"  batch=9 补充: {sum(1 for c in cards if c.get('batch')==9)}/{len(cards)}")
print(f"  Vue CLI 端口修正 (5173→8080): {vue_port_fixes} 张")
print(f"输出: {OUTPUT}")
