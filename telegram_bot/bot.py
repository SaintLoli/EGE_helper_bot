from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import telegram
from telegram_bot._parser import Parser
from .database import DB


class TelegramBot:
    TOKEN = 'TOKEN'  # ENTER YOUR BOT TOKEN HERE
    PARSER = Parser()
    DATABASE = DB()

    def __init__(self):
        updater = Updater(self.TOKEN)
        dp = updater.dispatcher

        choose_sub = ConversationHandler(
            entry_points=[CommandHandler('watchexamlist', self.watchexamlist)],
            states={
                'choice': [MessageHandler(Filters.text & ~Filters.command, self.you_choose)]
            },
            fallbacks=[CommandHandler('stop', self.stop)]
        )

        create_user = ConversationHandler(
            entry_points=[CommandHandler('register', self.register)],
            states={
                'add_user': [MessageHandler(Filters.text & ~Filters.command, self.add_user)]
            },
            fallbacks=[CommandHandler('stop', self.stop)]
        )

        dp.add_handler(CommandHandler('start', self.start))
        dp.add_handler(CommandHandler('help', self.help))
        dp.add_handler(CommandHandler('checkregister', self.checkregister))
        dp.add_handler(create_user)
        dp.add_handler(choose_sub)

        updater.start_polling()
        updater.idle()

    def help(self, update, context):
        command_list = "\n".join(['/' + i for i in dir(self) if '__' not in i])
        update.message.reply_text(
            f'{command_list}'
        )

    def stop(self, update, context):
        return ConversationHandler.END

    def start(self, update, context):
        update.message.reply_text(
            '<i><b>Данный бот создан в учебных целях;\n'
            'Все материалы взяты из открытого банка заданий ФИПИ;\n'
            'Все материалы будут незамедлительно удалены по просьбе правообладателей</b></i>',
            parse_mode=telegram.ParseMode.HTML
        )

    def you_choose(self, update, context):
        update.message.reply_text(f'Вы выбрали следующие предметы: {update.message.text}')
        return ConversationHandler.END

    def watchexamlist(self, update, context):
        update.message.reply_text('Выберите предмет по которому вы хотите сдавать экзамен\n\n\n'
                                  f'{self.PARSER.get_subject_list()}')
        return 'choice'

    def register(self, update, context):
        update.message.reply_text(
            'Сейчас мы попросим вас зарегестрироваться в системе:\n'
            'Введите адрес электронной почты и пароль в формате\n'
            '<b>mail@domain.com:password</b>', parse_mode=telegram.ParseMode.HTML
        )
        return 'add_user'

    def add_user(self, update, context):
        mail, pas = update.message.text.split(':')
        if update.message.from_user.last_name:
            username = update.message.from_user.first_name + ' ' + update.message.from_user.last_name
        else:
            username = update.message.from_user.first_name

        self.DATABASE.create_user(
            update.message.from_user.id, username, mail, pas
        )

    def checkregister(self, update, context):
        user = self.DATABASE.check_user(update.message.from_user.id)
        print(user.name)
        if user:
            update.message.reply_text(f'Здравствуйте, {user.name}')