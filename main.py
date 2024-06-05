import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InputFile
import requests

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
USER = os.getenv("USER_ID")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

ADMINS = [int(USER)]





@dp.message_handler(commands="start")
async def start(message: types.Message):
    #     kb = [
    #         [types.KeyboardButton(text="Button1")],
    #         [types.KeyboardButton(text="Button2")]
    #     ]
    #     keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Text on field")
    #     await message.answer("Which button push", reply_markup=keyboard)

    logging.info(f"Користувач {message.from_user.first_name} з нікнеймом {message.from_user.username} "
                 f"натиснув команду {message.text}")


    await message.answer(text='Привіт! Я - бот-завантажувач🎲\nНадішли мені посилання на TikTok-відео, і я відправлю його тобі без водяного знаку!')

@dp.message_handler()
async def start(message: types.Message):
    link = message.text

    msg = await message.answer("Будь ласка зачекайте, оброблюємо ваш запит.")
    url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

    querystring = {"url": "https://www.tiktok.com/@tiktok/video/7231338487075638570", "hd": "1"}
    headers = {
        "x-rapidapi-key": "e3ab95d0c4msh613ec78e56ee0f4p1d93d3jsn4ea37aa0c9a7",
        "x-rapidapi-host": "tiktok-video-no-watermark2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    video_link = response.json()['data']['play']
    await msg.edit_text("Надсилаємо відео. \nЗачекайте...")
    await msg.delete()
    await message.answer_video(InputFile(video_link))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

