import types
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from aiogram.types import Message, CallbackQuery
from config import dp
from keyboards import *
import logging
import os
from keyboards import *
import random

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start(msg: Message):
    img = open('rasm/headphones.jpg', 'rb')
    await msg.answer_photo(img, reply_markup=menu1)

count = []
# bitta knopkaga schotchik like/dislike
@dp.callback_query_handler(Text('like_dislike'))
async def likes(call: CallbackQuery):
    if call.from_user.id not in count:
        count.append(call.from_user.id)
        await call.answer('Like!')
    elif call.from_user.id in count:
        await call.answer('Dislike!')
        count.pop()

@dp.callback_query_handler(text='cancel')
async def cancel(call:CallbackQuery):
    await call.message.delete()

class Next_Button:
    @dp.callback_query_handler(text='next1')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu2)

    @dp.callback_query_handler(text='next2')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu3)

    @dp.callback_query_handler(text='next3')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu4)

    @dp.callback_query_handler(text='next4')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu5)

    @dp.callback_query_handler(text='next5')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu6)

    @dp.callback_query_handler(text='next6')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu7)

    @dp.callback_query_handler(text='next7')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu8)

    @dp.callback_query_handler(text='next8')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu9)

class Back_Button:
    @dp.callback_query_handler(text='back1')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu1)

    @dp.callback_query_handler(text='back2')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu2)

    @dp.callback_query_handler(text='back3')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu3)

    @dp.callback_query_handler(text='back4')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu4)

    @dp.callback_query_handler(text='back5')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu5)

    @dp.callback_query_handler(text='back6')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu6)

    @dp.callback_query_handler(text='back7')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu7)

    @dp.callback_query_handler(text='back8')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu8)

    @dp.callback_query_handler(text='back9')
    async def next(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=menu9)

class First_menu:
    @dp.callback_query_handler(text='1')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/16 Mockingbird.m4a', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='2')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Akon – Lonely.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='3')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Don_omar_ft_Lucenzo,_Daddy_yankee.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='4')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Messiah - Solito (Lonely) ft_ Nicky Jam _ Akon [ L8BswQ-qfvY.m4a', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='5')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Right Now (Na Na Na) CD 1 TRACK 1 (128).mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)

class Second_menu:
    @dp.callback_query_handler(text='6')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Aventura - All Up 2 You (feat_ Akon_ Wisin _ Yan xN6n85y04ug.m4a', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)

    @dp.callback_query_handler(text='7')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/I ll Still Kill (Instrumental)   50 Cent, Akon.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='8')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/06. Billie Jean.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='9')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open("musiqa/They don't care about us.mp3", 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='10')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/10 - Much To Soon.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)

class Third_menu:
    @dp.callback_query_handler(text='11')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Sami Yusuf – Allah.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='12')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Bellie_Eilish-Bad_Guy.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='13')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Dawlati Baqia   Nasheed.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='14')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/bellie eilish - therefore.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='15')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Lana Del Rey - Dark Paradise.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)

class Fourth_menu:
    @dp.callback_query_handler(text='16')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Lost in Paradise - Джоанна Ванг.m4a', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)

    @dp.callback_query_handler(text='17')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Nashid_-_Best_ – Jundullah_Nasheed.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='18')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Alice In Chains - Would    Burnout Paradise OST.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='19')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open("musiqa/Sami Yusuf - Ya Nabi (Live) ( 256kbps cbr ).mp3", 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)


    @dp.callback_query_handler(text='20')
    async def one(call: CallbackQuery):
        await call.answer(cache_time=15)
        msc = open('musiqa/Ummon_-_Osmon.mp3', 'rb')
        await call.message.answer_audio(msc, reply_markup=like_dislike_buttons)





if __name__ == '__main__':
    executor.start_polling(dp)