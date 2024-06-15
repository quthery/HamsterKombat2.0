from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from random import randint as rn
import app.keyboards as kb
from app.rep import MangaRepository
import os



clicks = 0


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await MangaRepository.add_one(id=message.from_user.id, first_name=message.from_user.first_name, last_name=message.from_user.last_name, full_name=message.from_user.full_name)
    await message.answer(f'Привет {message.from_user.first_name}\nВ этом боте ты сможешь майнить петуха',
                         reply_markup=kb.main)


@router.message(F.text == "Майнить петуха🐓(+1 коин)")
async def earning(message: Message):
    await MangaRepository.add_coins(id=message.from_user.id)
    coins = await MangaRepository.get_total_coins(id=message.from_user.id)
    await message.answer(f"+1 петушок\n твой баланс петушков: {coins}", reply_markup=kb.follow)


@router.message(F.text == "Личный кабинет💻")
async def user_profile(message: Message):
    total_coins = await MangaRepository.get_total_coins(id=message.from_user.id)

    profile_message = f"🌟 **Личный кабинет пользователя {message.from_user.full_name}**\n\n"
    profile_message += f"💰 **Баланс петушков:** {total_coins}\n\n"
    profile_message += "🎉 **Спасибо, что выбрали нашего бота!**"

    await message.answer(profile_message)

@router.message(F.text == "FAQ📘")
async def earning(message: Message):
    await message.answer("тут ответы на твои вопросы!:\nhttps://telegra.ph/CHasto-zadavaemye-voprosy-PetyaKombatbot-06-15")




@router.callback_query(F.data == "Mining")
async def mining(callback: CallbackQuery):
    callback.answer()