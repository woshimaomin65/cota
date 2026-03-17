import logging
import copy
from message_local import Message
from cota.store import Store
from cota.channels.channel import Channel
from action_local import Action
from typing import Text, List, Dict, Any, Optional, Callable, Iterable, Awaitable, NoReturn
from dst_local import DST
from cota.actions.bot_utter import BotUtter
from cota.actions.form import Form
logger = logging.getLogger(__name__)

class Processor:
    def __init__(
            self,
            agent: 'Agent',
            store: Store
    ):
        self.agent = agent
        self.store = store
        self.dst = None  # todo

    def _get_dst(self):
        pass

    def _update_dst(self):
        pass

    async def handle_message(
            self,
            message: Message,
            channel: Optional[Channel] = None
    ):
        """handle message"""
        if self.agent.dialogue.get('use_proxy_user') == True:
            await self._handle_message_proxy(message, channel)
            return

        action = Action.build_from_name(name='UserUtter')
        action.run_from_dict({
            "result": [message.as_dict()],
            "sender": message.sender or 'user',
            "sender_id": message.sender_id or 'default_user',
            "receiver": message.receiver or 'bot',
            "receiver_id": message.receiver_id or 'default_bot'
        })

        if channel:
            await self.execute_channel_effects(action, message.session_id, channel)

        self.dst = DST(session_id=message.session_id, agent=self.agent)
        self.dst.update(action)

        #if message.receiver != 'bot':
        #    await self.save_tracker(self.dst)
        #    return
        await self._handle_bot_actions(message.session_id, channel)

    async def _handle_bot_actions(self, session_id: Text, channel: Optional[Channel] = None):
        while True:
            breakpoint()
            bot_actions = await self.agent.generate_actions(self.dst)
            for action_item in bot_actions:
                # All actions are single actions now (no tuple handling)
                await action_item.run(self.agent, self.dst)
                self.dst.update(action_item)
                logger.debug(f"After DST updated: \n {self.dst.current_state()}")
                if channel:
                    await self.execute_channel_effects(action_item, session_id, channel)
                if isinstance(action_item, BotUtter):
                    return
            if len(bot_actions) > 1 and isinstance(bot_actions[-1], Form) and isinstance(bot_actions[-2], BotUtter):
                break

    async def execute_channel_effects(
            self,
            action: Action,
            session_id: Text,
            channel: Channel,
    ) -> None:
        for res in action.result:
            await channel.send_response(session_id, copy.deepcopy(res))
