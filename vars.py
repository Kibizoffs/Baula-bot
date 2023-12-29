import asyncio

from config import *

FATAL_ERROR = 'FATAL ERROR'
NIL = 'nil'
OSTANOV = 'ОСТАНОВ: '

amount_of_msgs = 'Кол-во сообщений в группе за эту неделю: <b>{}</b>\n'
stop_baula = 'Я ушёл есть мороженое (но обещаю вернуться) 🍦'

too_long_msg = f'{OSTANOV}слишком длинная string 😐'
empty_msg = f'{OSTANOV}nil сообщение 😂'
bad_nums = f'{OSTANOV}плохие числа 🥺'
edit_updated = 'Значение была обновлена 😎'
edit_key_not_found = f'{OSTANOV}ключ не была найдена 😔'
edit_group_doesnt_exist = f"""{OSTANOV} эта группа не была найдена.\nДоступные: {', '.join(f"'{str(x)}'" for x in baula_rubl_sal_groups)}"""
edit_wrong_last_name_format = f'{OSTANOV}плохой формат фамилии 🤬. Только кириллица!'
register_already = f'{OSTANOV}ты уже зарегистрирована 🥴'
register_ok = 'Регистрация прошла успешно 🤪\n'
register_not_yet = f'{OSTANOV}ты ещё не была зарегистрирована 😵'
delete_confirm = 'Подтвердите удаление 🙁'
delete_cancelled = 'Удаление была отменена 🥰'
delete_ok = 'Удаление прошла успешно 🖕\n(да пребудет с тобой... {})'
not_in_group = F"{OSTANOV}ты не в группе. Присвой значение к ключу 'gr' через /edit 🤓"
not_in_rubl_prac_group = f'{OSTANOV}ты не в 107-ой или 108-ой группе. Шуруй отсюда 😝'
pe_rubl_large_nums = f'{OSTANOV}переполнение 😱'
pe_ok = 'Было: {} ⚽\nСтало: {} ⚽'
rubl_ok = 'Было: {}₽\nСтало: {}₽'

no_user = f'{OSTANOV}юзер не был найден 😯'
no_profile_photo = f'{OSTANOV}поставь фото на аву (А.Н.Сальникову срочно нужно) 😫'
sal_2_arguments = f'{OSTANOV}укажи 2 юзер ID 😤'
trash_memory = 'Память:'
trash_text = 'Сборщик мусора ПАСКАЛЬ-МАШИНЫ обнаружила эту нечисть 😬'

base_bad_base = f'{OSTANOV}плохая СС. 1 <= СС <= 16. Пример: 2-16'
base_bad_num = f'{OSTANOV}плохая число'
base_ok = '<code>{}</code> из {}-ой системы в {}-ую:\n<code>{}</code>'
qr_ok = 'QR-код по запросу:'
qr_cant_generate = f'{OSTANOV}не смог быть сгенерирован 🥶'
random_bad_scope = f'{OSTANOV}плохая диапазон. Пример: 1-10'
random_bad_amount = f'{OSTANOV}плохая кол-во. 1 <= кол-во <= 10'
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
passport_baula = '\nБаулкоины:\n  {}₿'
passport_rubl = '\nИстория:\n  {}₽'
passport_sal = '\nПросрок:\n  {} дн(я/ей)'
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

    '/base <старая СС>-<новая СС> <число>\n' +
    '  перевести число из одной СС в другую\n' +
    '/math <выражение>\n' +
    '  ПАСКАЛЬ-МАШИНА посчитает всё! (но не точно)\n' +
    '/qr <текст>\n' +
    '  сгенерировать КУАР-код\n' +
    '/random <диапазон> <кол-во чисел>\n' +
    '  сгенерировать рандомные числа\n' +
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
    'Пример: <code>/edit {} Кибизов</code>'
)
