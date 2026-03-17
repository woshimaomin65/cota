#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cota 天气机器人快速启动脚本
"""

import sys
import os
import asyncio

# 添加 cota 到路径
sys.path.insert(0, '/Users/maomin/programs/vscode/cota')

from cota.agent import Agent
from cota.channels.cmdline import Cmdline

async def main():
    print("=" * 60)
    print("🌤️  Cota 天气机器人")
    print("=" * 60)
    print("")
    
    # 加载 agent 配置
    config_path = "/Users/maomin/programs/vscode/cota/cota/bots/weather"
    
    print(f"📂 配置路径：{config_path}")
    print(f"🔑 LLM: aliyun-codingplan (qwen3.5-plus)")
    print("")
    
    try:
        # 加载 Agent
        print("⏳ 正在加载 Agent...")
        agent = Agent.load_from_path(path=config_path)
        print("✅ Agent 加载成功！")
        print("")
        
        # 显示配置信息
        print("📋 可用 Actions:")
        for action_name in agent.actions.keys():
            print(f"  - {action_name}")
        print("")
        
        print("=" * 60)
        print("💬 开始对话（输入'退出'结束）")
        print("=" * 60)
        print("")
        
        # 创建命令行 channel
        async def handler(message, channel):
            await agent.processor.handle_message(message, channel)
        
        cmdline_channel = Cmdline(on_new_message=handler)
        await cmdline_channel.on_connect()
        
    except KeyboardInterrupt:
        print("\n\n👋 再见！")
    except Exception as e:
        print(f"❌ 错误：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
