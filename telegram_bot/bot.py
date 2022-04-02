from telegram.ext import Updater, CommandHandler
import telegram
from _parser import Parser


class TelegramBot:
    TOKEN = 'TOKEN'
    PARSER = Parser()

    def __init__(self):
        updater = Updater(self.TOKEN)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler('start', self.start))
        dp.add_handler(CommandHandler('watchexamlist', self.watchexamlist))

        updater.start_polling()
        updater.idle()

    def start(self, update, context):
        update.message.reply_text(
            '<i><b>Данный бот создан в учебных целях;\n'
            'Все материалы взяты из открытого банка заданий ФИПИ;\n'
            'Все материалы будут незамедлительно удалены по просьбе правообладателей</b></i>',
            parse_mode=telegram.ParseMode.HTML
        )

    def watchexamlist(self, update, context):
        update.message.reply_text(self.PARSER.get_subject_list())