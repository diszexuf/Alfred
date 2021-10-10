import asyncio
from aiogram import Bot, Dispatcher, types, executor
import os
from dotenv import dotenv_values

config = dotenv_values(".env")

# async def start_handler(event: types.Message):
#     await event.answer(
#         f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
#         parse_mode=types.ParseMode.HTML,
#     )
#
# async def category_handler(event: types.Message):
#     await event.answer(
#
#     )
#
#
# async def main():
#     bot = Bot(token=config['TELEGRAM_TOKEN'])
#     try:
#         disp = Dispatcher(bot=bot)
#         disp.register_message_handler(start_handler, commands={"start", "restart"})
#         disp.register_message_handler(category_handler, commands={"inf", "op"})
#         await disp.start_polling()
#     finally:
#         await bot.close()
#
# asyncio.run(main())


import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config['TELEGRAM_TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    text_and_data = (
        ('ОП', 'op'),
        ('ИНФА', 'inf'),
    )
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard_markup.row(*row_btns)
    await message.reply("Ну здарова, студент!\n4ё, куда идём?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='op')
async def inline_kb_answer_callback_op_handler(query: types.CallbackQuery):
    await bot.send_message(query.from_user.id, 'op')


@dp.callback_query_handler(text='inf')
async def inline_kb_answer_callback_inf_handler(query: types.CallbackQuery):
    # await bot.send_message(query.from_user.id, 'infa!')
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    text_and_data = (
        ('Check queue', 'check_inf'),
        ('Join in queue', 'join_inf'),
    )
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard_markup.row(*row_btns)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
