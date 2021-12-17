from aiogram import  types,Bot
from typing import Tuple, Any

from aiogram.contrib.middlewares.i18n import I18nMiddleware
from data.config import I18N_DOMAIN, LOCALES_DIR
from utils.db_api import quick_commands
from utils.db_api.quick_commands import select_user
from utils.db_api.schemas.user import User

async def get_language(user_id):
    user = await quick_commands.select_user(user_id)
    if user:
        return user.language

class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        bot = Bot.get_current()
        user_id = types.User.get_current().id
        return await get_language(user_id) or types.User.locale

def setup_middleware(dp):
    i18n = ACLMiddleware(I18N_DOMAIN,LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n