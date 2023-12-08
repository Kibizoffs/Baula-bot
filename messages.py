too_long_message = 'Слишком длинное сообщение'
empty_message = 'Пустое сообщение'
edit_deleted = 'Значение было удалено'
wrong_format = 'Неправильный формат'
edit_updated = 'Значение была обновлена'
edit_key_not_found = 'Ключ не был найден'
already_registered = 'Вы уже зарегистрированы'
register_ok = 'Регистрация прошла успешно'
not_yet_registered = 'Вы ещё не были зарегистрированы'
delete_ok = 'Удаление прошло успешно'
pe_rubl_err = 'Плохие числа'
pe_ok = 'Было {} ⚽. Стало {} ⚽'
rubl_ok = 'Было {}₽. Стало {}₽'

baula_text = (
    'id: <code>{}</code>\n' +
    'Юзернейм: {}\n' +
    "Библиотека: <a href='https://pypi.org/project/aiogram/'>Aiogram {}</a>\n" +
    "Хостинг: <a href='https://timeweb.cloud/r/kibizoffs1'>Timeweb</a>\n" +
    'Платформа: {}\n' +
    "Время работы: {}"
)

feedback_err = 'Ваше сообщение не было доставлено до администрации'
feedback_ok = 'Ваше сообщение было успешно отправлено администрации'

edit_text = ('/edit <ключ> <значение> - присвоить ключу значение\n' +
    "    'last_name'* <фамилия>\n" +
    "    'group_id'* <группа>\n" +
    "    'send_baula_res' <'0' (отключено) или '1' (включено)> - присылать результаты СР Баулы в ЛС\n" +
    "    'msg_count_1w' <'-1' (отключено) или '0' (включено)> - участвовать в статистике по сообщениям в группе")

help_text = ('Список команд\n\n' +
    '/start - меню команд\n' +
    '/baula - инфо о боте\n' +
    '/feedback <сообщение*> - отправить сообщение администрации\n\n' +

    '/passport - инфо о вас\n' +
    '/edit <ключ*> <значение*> - установить значение к ключу в записе о вас в базе данных\n' +
    '/register - зарегистрировать аккаунт\n' +
    '/delete - удалить аккаунт\n\n' +

    "/zachet <студент*> - 'зачёт, чувак!'\n" +
    '/pet <студент*> <препод> - похвалить')
