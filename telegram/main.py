import asyncio
from aiogram import Dispatcher,Bot
from config import config
from telegram.routers.messages import setup_router as message_router
bot = Bot(token=config.api_key)
dp = Dispatcher()
msg_router = message_router(bot=bot,config=config)
dp.include_router(msg_router)
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())