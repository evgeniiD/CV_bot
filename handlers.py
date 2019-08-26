from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction
from cv_bot import mytoken
from functools import wraps
from telegram.ext import ConversationHandler
import sqlite3

phone = mytoken.myphone
email = mytoken.mymail
NAME, COMPANY, IMPROVE = range(3)

conn = sqlite3.connect("final.db", check_same_thread=False)  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

#cursor.execute("""CREATE TABLE dbforfeedback
 #                 (id integer , name text, company text, improve text)
  #             """)

def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context, *args, **kwargs)

    return command_func


@send_typing_action
def start(update, context):
    cursor.execute("""insert into dbforfeedback (id)
    values (?) """, (update.message.chat_id,))
    conn.commit()
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='О, привет!')
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Вы попали на моего CV-бота.')
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Здесь я попытаюсь вкратце рассказать о себе и своих навыках')

    keyboard_for_start_bio = [[InlineKeyboardButton("Поехали!", callback_data='start_bio')]]
    reply_markup = InlineKeyboardMarkup(keyboard_for_start_bio)
    update.message.reply_text('Начнем?', reply_markup=reply_markup)


@send_typing_action
def button_for_start_bio(update, context):
    query = update.callback_query
    query.edit_message_text(text="Итак...".format(query.data))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Я студент СПБГЭТУ ЛЭТИ. ')
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='6 курс(специалитет) - направление компьютерная безопасность.')
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='За эти 6 лет я много чего опробовал( интересно было). ')
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='У меня есть опыт в ИБ, фронтэнде, и бэкэнде, а еще немного в AWS.')

    keyboard_to_calm_down = [[InlineKeyboardButton("Воу, воу полегче!!!!1", callback_data='calm_down')]]
    reply_markup = InlineKeyboardMarkup(keyboard_to_calm_down)
    query.message.reply_text('**Игнорируйте этот текст. Кнопку по другому не присобачить**', reply_markup=reply_markup)


@send_typing_action
def button_to_calm_down(update, context):
    query = update.callback_query
    query.edit_message_text(text="Ок, я понял, с чего начать?".format(query.data))

    keyboard_to_calm_down = [[InlineKeyboardButton("Фронтэнд", callback_data='front'),
                              InlineKeyboardButton("Бэкэнд", callback_data='back')],
                             [InlineKeyboardButton("ИБ", callback_data='IB'),
                              InlineKeyboardButton("AWS", callback_data='AWS')],
                             [InlineKeyboardButton("Все прочитано! Давай дальше.", callback_data='go_next')]]
    reply_markup = InlineKeyboardMarkup(keyboard_to_calm_down)
    query.message.reply_text('Расскажи мне про...', reply_markup=reply_markup)


@send_typing_action
def about_front(update, context):
    query = update.callback_query
    query.edit_message_text(text="Фронтэндом я занимался около 8 месяцев, по залету.".format(query.data))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Получилось поработать в компании преподователя и пройти летнюю стажировку в EPAM. '
                                'За это время изучил:JS,CSS,HTML,\n React(чуть-чуть). Удалось поработать с несколькими '
                                'CMS: MODX,Bitrix,Wordpress,\n Joomla(господи прости). Знаком с СУБД - MySQL.')

    keyboard_to_calm_down = [[InlineKeyboardButton("Фронтэнд", callback_data='front'),
                              InlineKeyboardButton("Бэкэнд", callback_data='back')],
                             [InlineKeyboardButton("ИБ", callback_data='IB'),
                              InlineKeyboardButton("AWS", callback_data='AWS')],
                             [InlineKeyboardButton("Все прочитано! Давай дальше.", callback_data='go_next')]]
    reply_markup = InlineKeyboardMarkup(keyboard_to_calm_down)
    query.message.reply_text('Расскажи мне про...', reply_markup=reply_markup)


@send_typing_action
def about_IB(update, context):
    query = update.callback_query
    query.edit_message_text(text="Это было давно(1-2 курс) и неправда.".format(query.data))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Увлекался пентестом по черному и не только. Участвовал в CTF на базе университета и не только.'
                                'Поработать нигде не довелось, так как учеба, все дела. Принимал участие в bug-bounty программах.'
                                'На 3 курсе проходил практику во ФСТЭКе. За те 2 месяца изучил 149фз.и 152фз. и познал некоторые таинства.')
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='У меня есть еще что рассказать, но это будет уже совсем не кратко.')

    keyboard_to_calm_down = [[InlineKeyboardButton("Фронтэнд", callback_data='front'),
                              InlineKeyboardButton("Бэкэнд", callback_data='back')],
                             [InlineKeyboardButton("ИБ", callback_data='IB'),
                              InlineKeyboardButton("AWS", callback_data='AWS')],
                             [InlineKeyboardButton("Все прочитано! Давай дальше.", callback_data='go_next')]]
    reply_markup = InlineKeyboardMarkup(keyboard_to_calm_down)
    query.message.reply_text('Расскажи мне про...', reply_markup=reply_markup)


@send_typing_action
def about_back(update, context):
    query = update.callback_query
    query.edit_message_text(text="То, чем я занимаюсь сейчас.".format(query.data))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Активно учу Python3. Весь этот бот написан на нем. '
                                'Из умений и знаний: git,mysql,django. '
                                'Типы данных, декораторы(тут они применяются), итераторы. Знаком с ООП. '
                                'Еще на первых курсах уника приходилось писать на C++. ')

    keyboard_to_calm_down = [[InlineKeyboardButton("Фронтэнд", callback_data='front'),
                              InlineKeyboardButton("Бэкэнд", callback_data='back')],
                             [InlineKeyboardButton("ИБ", callback_data='IB'),
                              InlineKeyboardButton("AWS", callback_data='AWS')],
                             [InlineKeyboardButton("Все прочитано! Давай дальше.", callback_data='go_next')]]
    reply_markup = InlineKeyboardMarkup(keyboard_to_calm_down)
    query.message.reply_text('Расскажи мне про...', reply_markup=reply_markup)


@send_typing_action
def about_aws(update, context):
    query = update.callback_query
    query.edit_message_text(text="Для души и просто полезно.".format(query.data))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='S3, EC2, LoadBalancer, VPC, CloudWatch, CloudTrail. '
                                'Примерно в октябре хочу пройти сертификацию на SAA. ')
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Если интересно, можем поболтать.')

    keyboard_to_calm_down = [[InlineKeyboardButton("Фронтэнд", callback_data='front'),
                              InlineKeyboardButton("Бэкэнд", callback_data='back')],
                             [InlineKeyboardButton("ИБ", callback_data='IB'),
                              InlineKeyboardButton("AWS", callback_data='AWS')],
                             [InlineKeyboardButton("Все прочитано! Давай дальше.", callback_data='go_next')]]
    reply_markup = InlineKeyboardMarkup(keyboard_to_calm_down)
    query.message.reply_text('Расскажи мне про...', reply_markup=reply_markup)


@send_typing_action
def go_next(update, context):
    query = update.callback_query
    query.edit_message_text(text="Знаю английский. Себя оцениваю на уровень"
                                 " где-то между В1 и В2. Ближе к В2. ".format(query.data))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Усидчивый, готов обучаться и впитывать как губка все новое. '
                                'Проблем с общением в коллективе не испытываю. '
                                'В перспективе, '
                                'хотел бы погрузиться в ML или Big Data. Мне эти темы безумно интересны.')
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Опыта работы как такового было мало, так как учеба(. ')
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='На этом, в прицнипе, всё. Мои контакты будут ниже. \n'
                                'Мейл: {0} \nМобильник: {1} \n'.format(email, phone))

    keyboard_for_bite = [[InlineKeyboardButton("Тык!", url='https://t.me/abellindsey')]]
    reply_markup = InlineKeyboardMarkup(keyboard_for_bite)
    query.message.reply_text('Вы можете написать мне прямо в tg: ', reply_markup=reply_markup)

    keyboard_for_brief_bio = [[InlineKeyboardButton("Еще один тык", callback_data='brief_bio')]]
    reply_markup = InlineKeyboardMarkup(keyboard_for_brief_bio)
    query.message.reply_text('Или же посмотреть всё, полезное вам,'
                             ' но в укороченном варианте. ', reply_markup=reply_markup)


@send_typing_action
def brief_bio(update, context):
    query = update.callback_query
    query.edit_message_text(text="Еще раз. Только кратко.".format(query.data))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Python3, django, git, mysql, типы данных, декораторы(тут они применяются '
                                'или скоро будут), '
                                'итераторы. Знаком с ООП. '
                                'Английский ближе к В2, усидчивый, быстро обучаюсь и хочу учиться. '
                                'Положил глаз на Big data и ML')

    keyboard_for_brief_bio = [[InlineKeyboardButton("Оставить фидбэк", callback_data='feed_back')]]
    reply_markup = InlineKeyboardMarkup(keyboard_for_brief_bio)
    query.message.reply_text('У меня к вам маааленькая просьба. Ответьте пожалуйста на три вопроса. ', reply_markup=reply_markup)


def feed_back(update, context):
    query = update.callback_query
    query.edit_message_text(text="Заранее спасибо!.".format(query.data))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Как вас зовут?')
    return NAME


def name(update, context):
    user_name = update.message.text
    cursor.execute("""update dbforfeedback set name = ? where id = ?""", (update.message.text, update.message.chat_id))
    conn.commit()
    context.bot.send_message(chat_id=update.message.chat_id, text="Из какой вы компании?")
    return COMPANY


def company(update, context):
    user_company = update.message.text
    cursor.execute("""update dbforfeedback set company = ? where id = ?""", (update.message.text, update.message.chat_id))
    conn.commit()
    context.bot.send_message(chat_id=update.message.chat_id, text="Как улучшить бота и информацию в нем?")
    return IMPROVE


def improve(update, context):
    user_improve = update.message.text
    cursor.execute("""update dbforfeedback set improve = ? where id = ?""", (update.message.text, update.message.chat_id))
    conn.commit()
    context.bot.send_message(chat_id=update.message.chat_id, text="Спасибо!")
    return ConversationHandler.END
