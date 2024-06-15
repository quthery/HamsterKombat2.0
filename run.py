import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import app.database as db
from app.handlers import router



async def main():
    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await db.create_tables()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Bot is active!")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")