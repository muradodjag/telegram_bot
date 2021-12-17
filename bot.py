from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import executor
import handlers
from calculator_func.rate_API import request_xml
from loader import storage, dp, db, bot
from utils.db_api import db_gino
from utils.db_api.db_gino import create_db

scheduler = AsyncIOScheduler()


def schedule_jobs():
    scheduler.add_job(request_xml,"interval",hours = 1)

async def on_startup(dp):
    import middlewares
    middlewares.setup(dp)
    schedule_jobs()
    print("Db is created")
    await create_db()
    await bot.close()



if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)

