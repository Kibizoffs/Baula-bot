# самое ироничное
FATAL_ERROR = 'FATAL ERROR'
NIL = 'nil'
OSTANOV = 'ОСТАНОВ: '

# ключи в БД
id_key = 'id'
gr_key = 'gr'
last_name_key = 'last_name'
pe_key = 'pe'
rubl_key = 'rubl'
msg_count_1w_key = 'msg_count_1w'

# группы
rubl_prac_groups = [107, 108]

amount_of_msgs = 'Кол-во сообщений в группе за эту неделю: 😲{}😛\n'

too_long_msg = f'{OSTANOV}слишком длинная string 😐'
empty_msg = f'{OSTANOV}nil сообщение 😂'
edit_updated = 'Значение была обновлена 😎'
edit_key_not_found = f'{OSTANOV}ключ не была найдена 😔'
edit_wrong_gr_format = f'{OSTANOV}плохой формат группы 🥵. 3 циферки написать не можешь?'
edit_group_doesnt_exist = f"""{OSTANOV} эта группа не была найдена.\nДоступные: {', '.join(f"'{str(x)}'" for x in rubl_prac_groups)}"""
edit_wrong_last_name_format = f'{OSTANOV}плохой формат фамилии 🤬. Только кириллица!'
already_registered = f'{OSTANOV}ты уже зарегистрирована 🥴'
register_ok = 'Регистрация прошла успешно 🤪\n'
not_yet_registered = f'{OSTANOV}ты ещё не была зарегистрирована 😵'
delete_confirm = 'Подтвердите удаление 🙁'
delete_cancelled = 'Удаление была отменена 🥰'
delete_ok = 'Удаление прошла успешно 🖕\n(да пребудет с тобой... {})'
not_in_group = F"{OSTANOV}ты не в группе. Присвой значение к ключу 'gr' через /edit 🤓"
not_in_rubl_prac_group = f'{OSTANOV}ты не в 107-ой или 108-ой группе. Шуруй отсюда 😝'
pe_rubl_bad_nums = f'{OSTANOV}плохие числа 🥺'
pe_rubl_large_nums = f'{OSTANOV}переполнение 😱'
pe_ok = 'Было: {} ⚽\nСтало: {} ⚽'
rubl_ok = 'Было: {}₽\nСтало: {}₽'

path_hand = 'Media/Hand/frame{}.png'
path_salnikov = 'Media/salnikov.jpg'
path_trash = 'Media/trash.jpg'
filename_hand = 'hand.gif'
filename_salnikov = 'salnikov.jpg'
filename_trash = 'trash.jpg'

no_profile_photo = f'{OSTANOV}поставь фото на аву (А.Н.Сальникову срочно нужно) 😫'
sal_2_arguments = f'{OSTANOV}укажи 2 юзер ID 😤'
trash_no_user = f'{OSTANOV}юзер не был найден 😯'
trash_memory = 'Память:'
trash_text = 'Сборщик мусора ПАСКАЛЬ-МАШИНЫ обнаружила эту нечисть 😬'

qr_ok = 'КУАР-код по запросу:'
yt_bad_url = f'{OSTANOV}плохая ссылка 🙄'
yt_ok = 'ютЬюб видео по запросу:'
yt_download = 'Скачать'
math_cant_parse = f'{OSTANOV}ПАСКАЛЬ-МАШИНА не смогла обработать твой байтовый мусор 🙃'
math_result = "Результат: {}\n<a href='{}'>Wolfram</a>"

feedback_err = f'{OSTANOV}твоё сообщение не была отправлена 😴'
feedback_ok = 'Твоё сообщение была отправлена 😏'

baula_txt = (
    'ID:\n  <code>{}</code>\n' +
    'Юзернейм:\n  @{}\n' +
    "Библиотека:\n  <a href='https://pypi.org/project/aiogram/'>Aiogram {}</a>\n" +
    "Хостинг:\n  <a href='https://timeweb.cloud/r/kibizoffs1'>Timeweb</a>\n" +
    'Платформа:\n  {}\n' +
    "Время работы:\n  {}"
)

id_ = 'ID:\n  <code>{}</code>'

chat_passport_gr = '\nГруппа:\n  <b>{}</b>'
passport_last_name = '\nФамилия:\n  {}'
passport_pe = '\nФизра:\n  {} ⚽'
passport_rubl = '\nИстория:\n  {}₽'
passport_msg_count_1w = '\nКол-во сообщений в группе за неделю:\n  {}'

help_txt = (
    'ОПИСАНИЕ ПРАВИЛ\n\n' +
    '/start\n' +
    '  меню команд\n' +
    '/baula\n'
    '  инфа о боте\n\n' +

    '/chat\n' +
    '  инфа о чате\n' +
    '/passport\n' +
    '  инфа о вас\n' +
    '/edit <ключ> <значение>\n' + 
    '  присвоить значение к ключу\n' +
    '/register\n' +
    '  зарегистрировать аккаунт\n' +
    '/delete\n' +
    '  удалить аккаунт\n' +
    '/pe <Δ баллов>\n'
    '  изменить свои мячи по физре\n' +
    '/rubl <Δ баллов>\n' +
    '  изменить свои рубли у Д.И.Рублёва\n\n' +

    '/hand <юзер ID>\n' +
    '  всемогущая рука сами знаете кого!\n' +
    '/sal <юзер ID> <юзер ID>\n' +
    '  судить А.Н.Сальникову\n' +
    '/trash <юзер ID>\n' +
    "  'не ботан, а ботяра!'\n\n" +

    '/math <выражение>\n' +
    '  ПАСКАЛЬ-МАШИНА посчитает всё! (но не точно)\n' +
    '/qr <текст>\n' +
    '  сгенерировать КУАР-код\n' +
    '/yt <ссылка>\n' +
    '  получить ссылку на скачивание ютЬюб видео\n\n' +

    '/feedback <сообщение>\n' +
    '  обратная связь'
)

edit_txt = (
    '/edit &lt;ключ&gt; &lt;значение&gt;\n\n' +
    'ключи:\n' +
    "  '{}' &lt;группа&gt;\n" +
    "  '{}' &lt;фамилия&gt;\n\n" +
    'Пример: <code>/edit {} 107</code>\n' +
    'Пример: <code>/edit {} Иванов</code>'
)
