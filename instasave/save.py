from aiogram import types, Bot, executor, Dispatcher
import logging
from aiogram.dispatcher.filters import Text
from insta import instagram_download

BOT_TOKEN = "6416363680:AAEpCGVqktAKMj7wc5ANDr7TONc-rvDFzhU"
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start(message: types.Message):

    await message.answer("Assalamu alaykum instagramdan video yuklovchi botga xush kelibsiz")


@dp.message_handler(Text(startswith="https://www.instagram.com/"))
async def insta_bot(message: types.Message):
    data = instagram_download(link=message.text)
    if data["type"] == "image":
        await message.answer_photo(photo=data["media"])
    elif data["type"] == "video":
        await message.answer_video(video=data["media"])
    elif data["type"] == "carousel":
        for i in data['media']:
            await message.answer_document(document=i)
    else:
        await message.answer("error")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
