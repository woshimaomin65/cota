#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cota 天气机器人简化测试
"""

import sys
import os
import asyncio

sys.path.insert(0, '/Users/maomin/programs/vscode/cota')

from cota.agent import Agent
from cota.message.message import Message

async def test():
    print("=" * 70)
    print("🌤️  Cota 天气机器人测试")
    print("=" * 70)
    print("")
    
    config_path = "/Users/maomin/programs/vscode/cota/cota/bots/weather"
    agent = Agent.load_from_path(path=config_path)
    
    print("✅ Agent 加载成功")
    print(f"   LLM: {list(agent.llms.keys())}")
    print(f"   Actions: {list(agent.actions.keys())}")
    print("")
    
    # 测试消息
    test_messages = [
        "你好",
        "北京天气怎么样",
    ]
    
    print("=" * 70)
    print("开始对话测试")
    print("=" * 70)
    print("")
    
    for msg_text in test_messages:
        print(f"👤 用户：{msg_text}")
        
        # 创建消息
        user_msg = Message(
            sender="user",
            sender_id="test_user",
            receiver="bot",
            text=msg_text
        )
        
        # 简单的消息处理
        from cota.channels.channel import Channel
        
        class SimpleChannel:
            def __init__(self):
                self.responses = []
            
            async def send(self, message):
                if isinstance(message, Message):
                    self.responses.append(message.text)
                    print(f"🤖 Bot: {message.text}")
                else:
                    self.responses.append(str(message))
                    print(f"🤖 Bot: {message}")
        
        channel = SimpleChannel()
        
        try:
            await agent.processor.handle_message(user_msg, channel)
        except Exception as e:
            print(f"⚠️  处理中：{type(e).__name__}")
        
        print("")
    
    print("=" * 70)
    print("✅ 测试完成")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(test())
