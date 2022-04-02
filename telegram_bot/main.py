from bot import TelegramBot
import logging

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG, filename='example.log'
    )

    logger = logging.getLogger(__name__)
    TelegramBot()