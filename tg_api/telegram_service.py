import logging

import telegram

__all__ = ("TelegramService")

logger = logging.getLogger(__name__)


class TelegramService:
    def __init__(self, token: str, chat_id: str) -> None:
        self.__bot = telegram.Bot(token=token)
        self.__chat_id = chat_id

    def send_text_message(self, text: str):
        logger.debug(f"TG send text message {text}")

        self.__bot.sendMessage(chat_id=self.__chat_id, text=text)
