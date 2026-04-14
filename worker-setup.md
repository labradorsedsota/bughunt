# BugHunt Worker 装机指南

> 新机器投入使用前，按以下顺序安装软件。所有 Worker 机器均为 Apple Silicon (M4) Mac。

---

## 1. 安装 VPN

按团队统一配置安装，确保能访问 GitHub 等外部资源。

## 2. 安装 Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**⚠️ 安装完成后，终端会输出类似以下提示（必须执行！否则 brew 命令找不到）：**

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

执行后验证：`brew --version`

## 3. 安装 Google Chrome

```bash
brew install --cask google-chrome
```

或从 https://www.google.com/chrome/ 下载安装。

## 4. 安装 Node.js + npm

```bash
brew install node
```

npm 随 Node.js 自动安装。

## 5. 安装 Git + gh CLI

```bash
brew install git gh
```

gh 首次使用需登录：`gh auth login`

## 6. 安装 mano-cua

按团队安装指引操作。

## 7. 检查清单

全部装完后逐项验证：

```bash
# VPN 连通性
curl -s -o /dev/null -w '%{http_code}' https://github.com   # 应返回 200

# Chrome 已安装
ls /Applications/Google\ Chrome.app   # 应存在

# Homebrew
brew --version

# Node + npm
node -v && npm -v

# Git + gh
git --version && gh --version

# mano-cua
mano-cua --version   # 或 mano-cua --help
```

全部通过后，Worker 环境就绪，可接收任务。

---

*文档版本：v1.0 | 2026-04-14 | Pichai*
