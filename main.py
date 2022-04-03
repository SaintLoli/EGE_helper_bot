from data import db_session
from telegram_bot.bot import TelegramBot
import logging
import os


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG, filename='telegram_bot/example.log'
    )

    db_path = str(os.getcwd()).replace(r'\telegram_bot', '', 1) + r'\db\helper.db'
    db_session.global_init(db_path)

    logger = logging.getLogger(__name__)
    TelegramBot()