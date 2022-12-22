from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import TOKEN
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

QUEST, CALC, COMPLEX = range(3)

def start (update, _):
    reply_keyboard = [['Рациональные', 'Комплексные']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Это калькулятор рациональных и комплексных чисел. Выбери из списка. Для отммены отправь /cancel', reply_markup=markup_key)
    return QUEST

def quest1 (update, _):
    update.message.reply_text('Введите выражение рациональных чисел в формате (2+3)*4/5', reply_markup=ReplyKeyboardRemove())
    return CALC

def quest2 (update, _):
    update.message.reply_text('Введите выражение комплексных чисел в формате (2+3j)*(4-5j)', reply_markup=ReplyKeyboardRemove())
    return COMPLEX

def cancel (update, _):
    update.message.reply_text('Конец. Напиши /start что бы начать.')
    return ConversationHandler.END

def get_calc(update, _):
    user = update.message.from_user
    message = update.message.text
    logger.info("calc %s: %s", user.username, message)
    update.message.reply_text(f'Результатом {message} будет {eval(message)}')

def get_complex(update, _):
    user = update.message.from_user
    message = update.message.text
    logger.info("complex %s: %s", user.username, message)
    update.message.reply_text(f'Результатом {message} будет {complex(eval(message))}')

upd = Updater(TOKEN)
disp = upd.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)], 
    states={
        QUEST: [MessageHandler(Filters.regex(r'Рациональные'), quest1), MessageHandler(Filters.regex(r'Комплексные'), quest2)],
        CALC: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, get_calc)],
        COMPLEX: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, get_complex)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

disp.add_handler(conv_handler)

upd.start_polling()
upd.idle()