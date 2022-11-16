from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


like_dislike_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='❤/💔', callback_data='like_dislike'),
            InlineKeyboardButton(text='❌', callback_data='cancel')
        ]
    ]
)
menu1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Eminem • Mockingbird', callback_data='1')
        ],
        [
            InlineKeyboardButton(text='Akon • Lonely', callback_data='2')
        ],
        [
            InlineKeyboardButton(text='Don Omar ft. Lucenzo, Daddy Yankee • Danza Kuduro (Remix)', callback_data='3')
        ],
        [
            InlineKeyboardButton(text='Messiah • Solito(Lonely) ft. Nicky Jam & Akon', callback_data='4')
        ],
        [
            InlineKeyboardButton(text='Akon • Right Now(Na Na Na)', callback_data='5')
        ],
        [
            InlineKeyboardButton(text='❌', callback_data='cancel'),
            InlineKeyboardButton(text='➡', callback_data='next1'),
        ]
    ]
)
menu2 = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            InlineKeyboardButton(text='Aventura • All Up 2 You(feat Akon, Wisin)', callback_data='6')
        ],
        [
            InlineKeyboardButton(text='50 cent, Akon • I Will Still Kill', callback_data='7')
        ],
        [
            InlineKeyboardButton(text='Michael Jackson • Billie Jean', callback_data='8')
        ],
        [
            InlineKeyboardButton(text='Michael Jackson • They do not care about us', callback_data='9')
        ],
        [
            InlineKeyboardButton(text='Michael Jackson • Much To Soon', callback_data='10')
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='back1'),
            InlineKeyboardButton(text='❌', callback_data='cancel'),
            InlineKeyboardButton(text='➡', callback_data='next2'),
        ]
    ]
)
menu3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Sami Yusuf • Allah', callback_data='11')
        ],
        [
            InlineKeyboardButton(text='Bellie Eilish • Bad Guy', callback_data='12')
        ],
        [
            InlineKeyboardButton(text='Dawlati Baqiya • Nasheed', callback_data='13')
        ],
        [
            InlineKeyboardButton(text='Bellie Eilish • Therefore', callback_data='14')
        ],
        [
            InlineKeyboardButton(text='Lana Del Ray • Paradise', callback_data='15')
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='back2'),
            InlineKeyboardButton(text='❌', callback_data='cancel'),
            InlineKeyboardButton(text='➡', callback_data='next3'),
        ]
    ]
)
menu4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Johanna Wang • Lost in Paradise', callback_data='16')
        ],
        [
            InlineKeyboardButton(text='Jundullah • Nasheed', callback_data='17')
        ],
        [
            InlineKeyboardButton(text='Alice • Would Burnout', callback_data='18')
        ],
        [
            InlineKeyboardButton(text='Sami Yusuf • Ya Nabi', callback_data='19')
        ],
        [
            InlineKeyboardButton(text='Ummon • Osmon', callback_data='20')
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='back3'),
            InlineKeyboardButton(text='❌', callback_data='cancel'),
            InlineKeyboardButton(text='➡', callback_data='next4'),
        ]
    ]
)
menu5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Bellie Eilish • Therefore', callback_data='14')
        ],
        [
            InlineKeyboardButton(text='Akon • Lonely', callback_data='2')
        ],
        [
            InlineKeyboardButton(text='Bellie Eilish • Bad Guy', callback_data='12')
        ],
        [
            InlineKeyboardButton(text='Messiah • Solito(Lonely) ft. Nicky Jam & Akon', callback_data='4')
        ],
        [
            InlineKeyboardButton(text='Akon • Right Now(Na Na Na)', callback_data='5')
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='back4'),
            InlineKeyboardButton(text='❌', callback_data='cancel'),
            InlineKeyboardButton(text='➡', callback_data='next5'),
        ]
    ]
)
menu6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Sami Yusuf • Allah', callback_data='11')
        ],
        [
            InlineKeyboardButton(text='Dawlati Baqiya • Nasheed', callback_data='13')
        ],
        [
            InlineKeyboardButton(text='Eminem • Mockingbird', callback_data='1')
        ],
        [
            InlineKeyboardButton(text='Lana Del Ray • Paradise', callback_data='15')
        ],
        [
            InlineKeyboardButton(text='Don Omar ft. Lucenzo, Daddy Yankee • Danza Kuduro (Remix)', callback_data='3')
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='back5'),
            InlineKeyboardButton(text='❌', callback_data='cancel'),
            InlineKeyboardButton(text='➡', callback_data='next6'),
        ]
    ]
)
menu7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Johanna Wang • Lost in Paradise', callback_data='16')
        ],
        [
            InlineKeyboardButton(text='Michael Jackson • They do not care about us', callback_data='9')
        ],
        [
            InlineKeyboardButton(text='Alice • Would Burnout', callback_data='18')
        ],
        [
            InlineKeyboardButton(text='Michael Jackson • Billie Jean', callback_data='8')
        ],
        [
            InlineKeyboardButton(text='Ummon • Osmon', callback_data='20')
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='back6'),
            InlineKeyboardButton(text='❌', callback_data='cancel'),
            InlineKeyboardButton(text='➡', callback_data='next7'),
        ]
    ]
)
menu8 = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            InlineKeyboardButton(text='Aventura • All Up 2 You(feat Akon, Wisin)', callback_data='6')
        ],
        [
            InlineKeyboardButton(text='Sami Yusuf • Ya Nabi', callback_data='19')
        ],
        [
            InlineKeyboardButton(text='50 cent, Akon • I Will Still Kill', callback_data='7')
        ],
        [
            InlineKeyboardButton(text='Jundullah • Nasheed', callback_data='17')
        ],
        [
            InlineKeyboardButton(text='Michael Jackson • Much To Soon', callback_data='10')
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='back7'),
            InlineKeyboardButton(text='❌', callback_data='cancel'),
            InlineKeyboardButton(text='➡', callback_data='next8'),
        ]
    ]
)
menu9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Akon • Right Now(Na Na Na)', callback_data='5')
        ],
        [
            InlineKeyboardButton(text='Eminem • Mockingbird', callback_data='1')
        ],
        [
            InlineKeyboardButton(text='50 cent, Akon • I Will Still Kill', callback_data='7')
        ],
        [
            InlineKeyboardButton(text='Sami Yusuf • Ya Nabi', callback_data='19')
        ],
        [
            InlineKeyboardButton(text='Jundullah • Nasheed', callback_data='17')
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='back8'),
            InlineKeyboardButton(text='❌', callback_data='cancel'),
        ]
    ]
)
