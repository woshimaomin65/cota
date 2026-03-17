#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cota 天气机器人完整测试
模拟用户查询天气的完整流程
"""

import sys
import os
import asyncio
import yaml

# 添加 cota 到路径
sys.path.insert(0, '/Users/maomin/programs/vscode/cota')

from cota.agent import Agent
from cota.processor import Processor

async def test_weather_bot():
    print("=" * 60)
    print("🌤️  Cota 天气机器人测试")
    print("=" * 60)
    print("")
    
    # 加载 agent 配置
    config_path = "/Users/maomin/programs/vscode/cota/cota/bots/weather"
    
    print(f"📂 配置路径：{config_path}")
    print("")
    
    try:
        # 加载 Agent
        print("⏳ 正在加载 Agent...")
        agent = Agent.load_from_path(path=config_path)
        print("✅ Agent 加载成功！")
        print("")
        
        # 显示配置信息
        print("📋 配置信息:")
        print(f"  - LLM: {list(agent.llms.keys())}")
        print(f"  - Actions: {list(agent.actions.keys())}")
        print(f"  - Policies: {len(agent.policies)} 个策略")
        print("")
        
        # 测试对话
        print("=" * 60)
        print("🧪 开始对话测试")
        print("=" * 60)
        print("")
        
        # 测试用例 1: 打招呼
        print("📝 测试 1: 打招呼")
        print("用户：你好")
        result = await agent.processor.handle_message(
            message="你好",
            channel="test_channel"
        )
        print(f"Bot: {result}")
        print("")
        
        # 测试用例 2: 查询天气
        print("📝 测试 2: 查询天气")
        print("用户：北京天气怎么样？")
        result = await agent.processor.handle_message(
            message="北京天气怎么样？",
            channel="test_channel"
        )
        print(f"Bot: {result}")
        print("")
        
        print("=" * 60)
        print("✅ 测试完成！")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"❌ 测试失败：{e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_weather_bot())
    sys.exit(0 if success else 1)
