from aiogram import Router,types
from aiogram.filters import Command
def setup_router(bot,config):
    router = Router()


    @router.message(Command('start'))
    async def start(message: types.Message):
        await bot.send_message(config.chat_id, 'testmessage')
    return router