from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData

from loader import _

# # Создаем CallbackData-объекты, которые будут нужны для работы


menu_cd = CallbackData('show_menu', 'level', 'name_btn')


# С помощью этой функции будем формировать коллбек дату для каждого элемента меню, в зависимости от
# переданных параметров.
def make_callback_data(level, name_btn='0'):
    return menu_cd.new(level=level, name_btn=name_btn)


async def choose_lang():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()
    langs = ["Azərbaycan dili","Русский","English","Türkçe"]
    name_btn = ["lang_az","lang_ru","lang_en","lang_tr"]
    for i,lang in enumerate(langs):
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, name_btn=name_btn[i])
        markup.row(
            InlineKeyboardButton(text=_(lang), callback_data=callback_data)
        )
    return markup




# sozdaem funkciyu, kotoraya sozdayet glavnoye menu
async def main_menu(lang):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton(text=_('Calculator',locale=lang),
                             callback_data=make_callback_data(level=CURRENT_LEVEL + 1, name_btn='calc'))
    )
    markup.row(
        InlineKeyboardButton(text=_('Location',locale=lang),
                             callback_data=make_callback_data(level=CURRENT_LEVEL + 1, name_btn='location'))
    )
    markup.row(
        InlineKeyboardButton(text=_('Change the language',locale=lang), callback_data=make_callback_data(level=CURRENT_LEVEL - 1, name_btn='back'))
    )
    return markup


# funkciya kotoraya sozdaet knopku dlya gorodov
async def cities_keyboard():
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup()
    cities = [_('Baku'), _('Sumgait'), _('Ganja'), _('Other')]
    name_btn = [_('Baki'), _('Sumqayit'), _('Gence'), _('Diger')]
    for i, city in enumerate(cities):
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, name_btn=f'{name_btn[i]}')
        markup.row(
            InlineKeyboardButton(text=city, callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text=_("Back"),
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1, name_btn='back'))

    )
    return markup


# Funkciya kotoraya sozdaet knopku dlya vibora naliciya jidkosti
async def liquid_keyboard():
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    choices = [_('Yes'), _('No')]
    name_btn = [_('Yes'), _('No')]
    for i, choice in enumerate(choices):
        button_text = f'{choice}'
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, name_btn=f'{name_btn[i]}')
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(text=_('Back'), callback_data=make_callback_data(level=CURRENT_LEVEL - 1, name_btn='back'))
    )
    return markup


# Funkciya kotoraya sozdayet knopku dlya edinici izmereniya
async def unit_keyboards():
    CURRENT_LEVEL = 4
    markup = InlineKeyboardMarkup()
    units = [_('gr'), _('kg')]
    name_btn = [_('gr'), _('kg')]
    for i, unit in enumerate(units):
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, name_btn=f'{name_btn[i]}')
        markup.insert(
            InlineKeyboardButton(text=unit, callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(text=_('Back'), callback_data=make_callback_data(level=CURRENT_LEVEL - 1, name_btn='back'))
    )
    return markup

#funkciya kotoraya sozdaet  knopki kotoriye pokazivayutsya posle vvoda massi. User mojet povtorit vvod ili
# je vernutsya na glavnoye menu
async def repeat_or_main_menu():
    CURRENT_LEVEL = 6
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(text=_('Repeat the input'),
                             callback_data=make_callback_data(level=CURRENT_LEVEL - 1, name_btn='repeat'))
    )
    markup.row(
        InlineKeyboardButton(text=_('Back to the main menu'),
                             callback_data=make_callback_data(level=1, name_btn='main_menu'))
    )
    markup.row(
        InlineKeyboardButton(text=_('Change the language'),
                             callback_data=make_callback_data(level=0, name_btn='main_menu'))
    )

    return markup


# Tut ya sozdal funkciyu dlya knopki 'back'. Ona prinimaet tekushiy uroven,
# a v callback_data vozvrashaet predidushiy uroven
async def back_btn(current_level):
    CURRENT_LEVEL = current_level
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(text='Back',
                             callback_data=make_callback_data(level=CURRENT_LEVEL - 1, name_btn='back'))
    )
    return markup