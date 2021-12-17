from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(id:int,name: str):
    old_user = await select_user(id)
    if old_user:
        return old_user
    else:
        user = User(id=id,name=name)
        await user.create()


async def select_all_user():
    users = await User.query.gino.all()
    return users
async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()

    return user

async def select_language(id: int):
    user = await select_user(id)
    return user.language

async def set_language(language,id:int):
    user = await select_user(id)
    await user.update(language=language).apply()


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total