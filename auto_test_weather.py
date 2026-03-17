#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cota 天气机器人自动化测试
模拟真实用户对话流程
"""

import sys
import os
import asyncio

sys.path.insert(0, '/Users/maomin/programs/vscode/cota')

from cota.agent import Agent

async def test_conversation():
    print("=" * 70)
    print("🌤️  Cota 天气机器人 - 自动化对话测试")
    print("=" * 70)
    print("")
    
    config_path = "/Users/maomin/programs/vscode/cota/cota/bots/weather"
    
    print("📂 加载配置...")
    agent = Agent.load_from_path(path=config_path)
    print("✅ Agent 加载成功")
    print("")
    
    print("📋 配置信息:")
    print(f"  LLM: {list(agent.llms.keys())}")
    print(f"  Actions: {list(agent.actions.keys())}")
    print("")
    
    # 测试用例
    test_cases = [
        "你好",
        "北京天气怎么样？",
        "我想去成都旅游，天气如何",
    ]
    
    print("=" * 70)
    print("🧪 开始对话测试")
    print("=" * 70)
    print("")
    
    for i, user_input in enumerate(test_cases, 1):
        print(f"【测试 {i}】")
        print(f"👤 用户：{user_input}")
        
        try:
            # 创建简单的 channel 模拟
            from cota.channels.channel import Channel
            
            class TestChannel(Channel):
                def __init__(self):
                    self.messages = []
                
                async def send(self, message):
                    self.messages.append(message)
                    print(f"🤖 Bot: {message}")
            
            channel = TestChannel()
            
            # 处理消息
            from cota.message.message import UserMessage
            user_msg = UserMessage(text=user_input, channel="test")
            
            await agent.processor.handle_message(user_msg, channel)
            
            print("")
            
        except Exception as e:
            print(f"❌ 错误：{e}")
            import traceback
            traceback.print_exc()
            print("")
    
    print("=" * 70)
    print("✅ 测试完成！")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(test_conversation())
