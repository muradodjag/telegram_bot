import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import TOKEN
from utils.db_api.db_gino import db

from middlewares.language_middleware import setup_middleware

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Настроим i18n middleware для работы с многоязычностью
i18n = setup_middleware(dp)
# Создадим псевдоним для метода gettext
_ = i18n.gettext
# eto nujno dlya togo shto bi ukorotit kod