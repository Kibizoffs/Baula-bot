import aiogram
import asyncio
import os

from config import env_key_token
from logger import logger
from utils import get_time

start_time = get_time()
bot = aiogram.Bot(token=os.getenv(env_key_token))
dp = aiogram.Dispatcher()

if __name__ == '__main__':
    from Commands.admin import admin_router
    from Commands.bot import bot_router
    from Commands.db import db_router
    from Commands.fun import fun_router
    from Commands.special import special_router
    from Events.stats import stats_router, send_and_clear_stats
    dp.include_routers(
        admin_router, bot_router, db_router,
        fun_router, special_router, stats_router)

    asyncio.run(dp.start_polling(bot))

