#!/bin/bash
# Cota 项目虚拟环境激活脚本

echo "🚀 激活 Cota 虚拟环境..."

# 切换到项目目录
cd /Users/maomin/programs/vscode/cota

# 检查 .venv 是否存在（Poetry in-project 模式）⭐ 优先
if [ -d ".venv" ]; then
    echo "✅ 找到 .venv（Poetry），激活中..."
    source .venv/bin/activate
    
# 检查 venv 是否存在（手动创建模式）
elif [ -d "venv" ]; then
    echo "✅ 找到 venv，激活中..."
    source venv/bin/activate
    
# 使用 Poetry 虚拟环境
else
    echo "📦 使用 Poetry 虚拟环境..."
    VENV_PATH=$(poetry env info --path 2>/dev/null)
    if [ -n "$VENV_PATH" ]; then
        source "$VENV_PATH/bin/activate"
        echo "✅ 已激活：$VENV_PATH"
    else
        echo "❌ 未找到虚拟环境，请先运行：poetry install"
        exit 1
    fi
fi

echo ""
echo "🎉 虚拟环境已激活！"
echo "================================"
echo "Python: $(which python)"
echo "版本：$(python --version)"
echo ""
echo "可用命令:"
echo "  - cota shell --config=cota/bots/weather"
echo "  - python test_llm.py"
echo "  - python run_weather_bot.py"
echo ""
echo "退出环境：deactivate"
echo "================================"
