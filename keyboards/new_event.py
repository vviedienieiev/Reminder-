from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
event_frequency_type =InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Одноразова подія", callback_data="one_time_event")],
    [InlineKeyboardButton(text="Повторювана подія", callback_data="recurring_event")],
])


event_frequency_options = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кожен місяць", callback_data="1 month"), InlineKeyboardButton(text="Кожні 3 місяці", callback_data="3 months")],
    [InlineKeyboardButton(text="Кожні 6 місяців", callback_data="6 months"), InlineKeyboardButton(text="Кожен рік", callback_data="12 months")],
])

yes_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✔️", callback_data="yes"), InlineKeyboardButton(text="❌", callback_data="no")],
])