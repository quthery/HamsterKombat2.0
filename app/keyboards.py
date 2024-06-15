from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
  [KeyboardButton(text='Майнить петуха🐓(+1 коин)')],
  [KeyboardButton(text='Личный кабинет💻'), KeyboardButton(text='FAQ📘')],
],

  resize_keyboard=True,
  input_field_placeholder="Воспользуйтесь кнопками ниже")

follow = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text="Подписаться на тг петуха", url="https://t.me/+6kP425YTJe43Nzk6")]
]
  
)

mining = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text="Подписаться на тг петуха", url="https://t.me/+6kP425YTJe43Nzk6")]
] 
)