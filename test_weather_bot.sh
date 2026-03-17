#!/bin/bash
# Cota 天气机器人测试脚本

echo "🚀 启动 Cota 天气机器人测试..."
echo ""

# 激活虚拟环境
cd /Users/maomin/programs/vscode/cota
source venv/bin/activate

# 进入 weather 机器人配置目录
cd cota/bots/weather

echo "📂 当前目录：$(pwd)"
echo "📝 配置文件:"
echo "  - agent.yml (智能体配置)"
echo "  - endpoints.yml (LLM 配置)"
echo "  - policy/data.yml (对话策略)"
echo ""

echo "🧪 启动命令行交互模式..."
echo "💡 提示：输入'你好'或'成都天气怎么样'来测试"
echo "按 Ctrl+C 退出"
echo ""

# 启动 shell 模式
cota shell --config=. --debug
