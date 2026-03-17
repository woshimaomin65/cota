#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cota 天气机器人简单测试
测试 LLM 配置和基本的对话流程
"""

import sys
import os
import asyncio

# 添加 cota 到路径
sys.path.insert(0, '/Users/maomin/programs/vscode/cota')

from cota.llm.llm import LLM

# 配置 LLM（参考 Copaw 的配置）
llm_config = {
    "type": "openai",
    "model": "qwen3.5-plus",
    "key": "sk-sp-9744b2d2a3834fe1875f74fc43689dbf",
    "apibase": "https://coding.dashscope.aliyuncs.com/v1"
}

async def test_llm():
    print("🚀 测试 Cota LLM 配置...")
    print(f"配置：{llm_config}")
    print("")
    
    try:
        # 创建 LLM 实例
        llm = LLM(llm_config)
        print("✅ LLM 初始化成功！")
        print("")
        
        # 测试对话
        print("🧪 测试对话：'你好，请用一句话介绍你自己'")
        response = await llm.generate_chat(
            messages=[
                {"role": "system", "content": "你是一个天气助手"},
                {"role": "user", "content": "你好，请用一句话介绍你自己"}
            ],
            max_tokens=200
        )
        print(f"回复：{response}")
        print("")
        
        print("✅ 测试成功！Cota 可以正常使用阿里云灵码 API")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败：{e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_llm())
    sys.exit(0 if success else 1)
