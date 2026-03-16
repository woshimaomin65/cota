import sys
from cota.agent import Agent
from cota.message.message import Message
import uuid
from typing import Text, List, Dict, Any, Optional, Callable, Iterable, Awaitable, NoReturn

config_path = '../cota/bots/weather'
agent = Agent.load_from_path(path=config_path)

async def handler(message, channel):
    await agent.processor.handle_message(message, channel)

class Controller():
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
