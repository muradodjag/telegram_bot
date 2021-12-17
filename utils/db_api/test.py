# import asyncio
#
# from data import config
# from utils.db_api import quick_commands
# from utils.db_api.db_gino import db
#
#
# async def test():
#     await db.set_bind(config.POSTGRES_URI)
#     await db.gino.drop_all()
#     await db.gino.create_all()
#
#     print("Add User")
#     await quick_commands.add_user(1,"Mike")
#     await quick_commands.add_user(2, "John")
#     await quick_commands.add_user(3, "Sandy")
#     print("Done")
#
#     users = await quick_commands.select_all_user()
#     print(f"All users: {users}")
#
#     count_users = await quick_commands.count_users()
#     print(f"A number of users: {count_users}")
#
#     user = await quick_commands.select_user(id = 2)
#     print(f"Get user: {user}")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test())