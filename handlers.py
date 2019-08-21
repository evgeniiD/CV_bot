from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='О, привет!')
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Вы попали на моего CV-бота.')
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Здесь я попытаюсь вкратце рассказать о себе, своих навыках и '
                                                                  'об опыте работы.')

    keyboard_for_start_bio = [[InlineKeyboardButton("Поехали!", callback_data='start bio')]]
    reply_markup = InlineKeyboardMarkup(keyboard_for_start_bio)
    update.message.reply_text('Начнем?', reply_markup=reply_markup)


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
    query.message.reply_text('**Игнорируйте этот текст. Кнопку по другому не присобачить**',reply_markup=reply_markup)


def button_to_calm_down(update, context):
    query = update.callback_query
    query.edit_message_text(text="Ок, я понял, с чего начать?".format(query.data))

    keyboard_to_calm_down = [[InlineKeyboardButton("Фронтэнд", callback_data='front'),
                              InlineKeyboardButton("Бэкэнд", callback_data='back')],
                             [InlineKeyboardButton("ИБ", callback_data='IB'),
                              InlineKeyboardButton("AWS", callback_data='AWS')],
                             [InlineKeyboardButton("Все прочитано! Давай дальше.",callback_data='go_next')]]
    reply_markup = InlineKeyboardMarkup(keyboard_to_calm_down)
    query.message.reply_text('Расскажи мне про...', reply_markup=reply_markup)


def about_front(update, context):
    query = update.callback_query
    query.edit_message_text(text = "Фронтэндом я занимался около 8 месяцев, по залету.".format(query.data))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Получилось поработать в компании преподователя и пройти летнюю стажировку в EPAM. '
                                'За это время изучил:JS,CSS,HTML,\n React(чуть-чуть). Удалось поработать с несколькими '
                                'CMS: MODx,Bitrix,Wordpress,\n Joomla(господи прости). Знаком с СУБД - MySQL.')

    keyboard_to_calm_down = [[InlineKeyboardButton("Фронтэнд", callback_data='front'),
                              InlineKeyboardButton("Бэкэнд", callback_data='back')],
                             [InlineKeyboardButton("ИБ", callback_data='IB'),
                              InlineKeyboardButton("AWS", callback_data='AWS')],
                             [InlineKeyboardButton("Все прочитано! Давай дальше.", callback_data='go_next')]]
    reply_markup = InlineKeyboardMarkup(keyboard_to_calm_down)
    query.message.reply_text('Расскажи мне про...', reply_markup=reply_markup)


def about_IB(update, context):
    query = update.callback_query
    query.edit_message_text(text = "Это было давно(1-2 курс) и неправда.".format(query.data))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Увлекался пентестом по черному и не только. Участвовал в CTF на базе университета и не только.'
                                'Поработать нигде не довелось, так как учеба, все дела. Принимал участие в bug-bounty программах.'
                                'На 3 курсе проходил практику во ФСТЭКе. За те 2 месяца изучил 149фз.и 152фз. и познал некоторые таинства')
    query.bot.send_message(chat_id=query.message.chat_id,
                           text='У меня есть еще что рассказать, но это будет уже совсем не кратко.')

    keyboard_to_calm_down = [[InlineKeyboardButton("Фронтэнд", callback_data='front'),
                              InlineKeyboardButton("Бэкэнд", callback_data='back')],
                             [InlineKeyboardButton("ИБ", callback_data='IB'),
                              InlineKeyboardButton("AWS", callback_data='AWS')],
                             [InlineKeyboardButton("Все прочитано! Давай дальше.", callback_data='go_next')]]
    reply_markup = InlineKeyboardMarkup(keyboard_to_calm_down)
    query.message.reply_text('Расскажи мне про...', reply_markup=reply_markup)
