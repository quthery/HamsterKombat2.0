from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from random import randint as rn
import app.keyboards as kb
import os



clicks = 0


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name} \n Толстый хомяк решил помайнить хомячка?\n',)
