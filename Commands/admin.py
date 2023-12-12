import aiogram
from aiogram.filters import Command
from aiogram.types import Message

from Events.messages import parse_msg
from config import admin_ids
from main import bot

admin_router = aiogram.Router()

@admin_router.message(Command(commands=['say', 'сказать']))
async def command_say(msg: Message):
    await parse_msg(msg)

    is_admin = False
    for admin_id in admin_ids:
        if msg.from_user.id == admin_id:
            is_admin = True
            break
    if is_admin:
        await msg.delete()
        if len(msg.text.split()) > 1:
            await msg.answer(
                text=' '.join(x for x in msg.text.split()[1:]),
                parse_mode='HTML'
            )
