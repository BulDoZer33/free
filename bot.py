from aiogram import Dispatcher, Bot, executor
from aiogram.types import Message
# Работа с фото
# from PIL import Image, ImageDraw


from config import *
from editing import *

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: Message):
   await message.answer('Hello, send photos')

# Сохранение и обработка фотографии
@dp.message_handler(content_types=['photo'])
async def editing_photo(message: Message):
   # Сохранение фотографии
   unique = message.photo[-1].file_unique_id # Уникальный id фото
   await message.photo[-1].download(f'photos/{unique}.jpg') # Сохранение

   # Обработка
   correct_color(f'photos/{unique}.jpg', (unique + '_result.jpg'))

if __name__ =='__main__':
   executor.start_polling(dp)