import sys
import os
from cota.agent import Agent
from cota.message.message import Message
from cota.channels.channel import Channel
import uuid
from typing import Text, List, Dict, Any, Optional, Callable, Iterable, Awaitable, NoReturn

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 配置路径（使用绝对路径）
config_path = os.path.join(script_dir, '..', 'cota', 'bots', 'weather')

agent = Agent.load_from_path(path=config_path)

async def handler(message, channel):
    await agent.processor.handle_message(message, channel)

class Controller(Channel):
    """命令行控制器，继承 Channel 以实现必要的接口"""
    
    def handle_text_message(self, sender_id:Text, text:Text, **kwargs: Any) -> Message:
        return Message(
            sender = 'user',
            sender_id = sender_id,
            receiver = kwargs.get("receiver", None),
            receiver_id = kwargs.get("receiver_id", None),
            session_id = kwargs.get("session_id", None),
            text = text,
            metadata = {}
        )

    def handle_message(self, message: Dict[Text, Any]) -> Message:
        """ handle client message """
        if message.get("type") == "text":
            return self.handle_text_message(message.pop("sender_id"), message.pop("text"), **message)

    async def send_text_message(self, recipient_id: Text, **kwargs: Any) -> None:
        """发送文本消息到控制台"""
        text = kwargs.get('text', '')
        if text:
            print(f"User: {text}")

    #async def send_image_url(self, recipient_id: Text, **kwargs: Any) -> None:
    #    """发送图片消息到控制台"""
    #    image_url = kwargs.get('image_url', '')
    #    if image_url:
    #        print(f"Bot: [图片] {image_url}")
    #    else:
    #        await self.send_text_message(recipient_id, **kwargs)

    async def agent_loop(self):
        """Handle the connection and continuously read messages from the command line."""
        session_id = uuid.uuid4().hex
        while True:
            print("Input message:")
            message = input().strip()
    
            if message == "/stop":
                sys.exit(0)
            message = {
                    'type': 'text',
                    'sender': 'user',
                    'sender_id': 'default_user',
                    'receiver': 'bot',
                    'receiver_id': 'default_bot',
                    'session_id': session_id,
                    'text': message,
                    'metadata': {}
                }
            message = self.handle_message(message)
            await handler(message, self)


if __name__ == "__main__":
    import asyncio
    
    print("🚀 启动 Cota 天气机器人 (manual 模式)...")
    print(f"📁 配置路径：{config_path}")
    print(f"🔍 绝对路径：{os.path.abspath(config_path)}")
    print("=" * 50)
    
    controller = Controller()
    
    try:
        asyncio.run(controller.agent_loop())
    except KeyboardInterrupt:
        print("\n\n👋 已退出机器人")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 发生错误：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
