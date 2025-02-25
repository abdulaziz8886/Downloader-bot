from aiogram import F, Bot, Dispatcher
from aiogram.types import Message, FSInputFile
import logging
from aiogram.filters import CommandStart
from config import bot_token
import asyncio, yt_dlp, os


logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def StartBot(message:Message):
    await message.answer('Assalomu Alaykum bo\'tdan foydalanishingiz mumkin')


@dp.message(F.text)
async def Yuklabot(message: Message):
    try:
        await message.answer('sizning videoningiz tayyorlanoqda ...')
        link = message.text
        video_options = {"format": "mp4","outtmpl": "video.%(ext)s"}
        with yt_dlp.YoutubeDL(video_options) as vida:
            info = vida.extract_info(link, download=True)
            filename = vida.prepare_filename(info)
        video1 = FSInputFile(filename)
        await message.answer_video(video=video1, caption="Mana marxamat sizning videoningiz !")
        os.remove(filename)
    except:
        await message.answer(' Afsuski Topilmadi')



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('tugadi')