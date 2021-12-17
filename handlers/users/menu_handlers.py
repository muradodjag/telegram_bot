import re
from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message


import keyboards.inline.menu_keyboards as kb
from calculator_func import calculator
from loader import dp, bot, _

from collections import defaultdict

from states.states import Test
from utils.db_api import quick_commands
from utils.misc import rate_limit

current_btn = defaultdict(list)# v etom slovare sohranayu znaceniya knopok kajdogo usera po chat id (poka shto drugogo nicego ne pridumal)

# srabativaniye na /start
@dp.message_handler(Command("start"), state="*")
async def show_button(message: types.Message, state: FSMContext):
    await state.finish() #esli vo vremya vvoda user vizovet komandu /start, to nujno zakrit state

    user_id = message.from_user.id
    current_btn[user_id].clear() #tut mi udalaem najatiya knopok
    name = message.from_user.full_name
    await quick_commands.add_user(id=user_id,name = name)
    await lang_menu(message)



# Funkciya kotoraya peredayet knopku s glavnim menu
async def lang_menu(message: Union[types.CallbackQuery, types.Message], **kwargs):
    markup = await kb.choose_lang()

    # esli u nas obyek message(t.e komanda start),to vipolnaetsya eta stroka
    if isinstance(message, Message):
        await message.answer(text=_("Choose a language"),
                             reply_markup=markup)

    # Если CallbackQuery - изменяем это сообщение
    elif isinstance(message, CallbackQuery):
        call = message
        user_id = call.from_user.id
        current_btn[user_id].clear()
        await call.message.edit_text(text=_('Choose a language'), reply_markup=markup)

async def main_menu_keyboards(callback: CallbackQuery, **kwargs):
    user_id = callback.from_user.id
    lang = await quick_commands.select_language(user_id)

    current_btn[user_id].clear()
    markup = await kb.main_menu(lang)
    await callback.message.edit_text(text=_('Hi,Can I help you?',locale=lang), reply_markup=markup)

# Funkciya kotoraya peredayet knopki s gorodami
async def cities(callback: CallbackQuery, **kwargs):
    markup = await kb.cities_keyboard()

    await callback.message.edit_text(text=_('Choose the city'), reply_markup=markup)


# Funkciya kotoraya peredayet knopki s edinicami izmereniya
async def unit(callback: CallbackQuery, **kwargs):
    markup = await kb.unit_keyboards()

    await callback.message.edit_text(text=_('Choose the unit'), reply_markup=markup)


# Funkciya kotoraya peredayet knopki s naliciem jidkosti v posilke
async def liguid(callback: CallbackQuery, **kwargs):
    markup = await kb.liquid_keyboard()

    await callback.message.edit_text(text=_('Do you have liquid in the parcel'), reply_markup=markup)

# Funkciya gde prosim polzovatelya vvesti massu posilki
async def user_input(callback: CallbackQuery, **kwargs):
    user_id = callback.from_user.id
    await callback.message.edit_text(_("Enter mass of product in {}").format(current_btn[user_id][-1]))
    await Test.Q1.set()



# tut mi lovim callback, kogda user najimaet na knopku 'location' i vivodim kartu s raspolojeniem ofisa
@dp.callback_query_handler(kb.menu_cd.filter(name_btn='location'))
async def location(call: CallbackQuery):
    user_id = call.from_user.id
    lang = await quick_commands.select_language(user_id)
    markup = await kb.main_menu(lang)
    await bot.send_location(call.message.chat.id, 40.417890792107606, 49.9362922625183)
    await call.message.answer(text=_('Hi,Can I help you?'), reply_markup=markup)


# Suda peredayutsya lubiye nayatiya na knopki
# I tut proishodit navigaciya po urovnyam
@dp.callback_query_handler(kb.menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")  # xranitsya tekushiy uroven knopki
    btn_name = callback_data.get("name_btn")  # xranitsya nazvaniye knopki
    user_id = call.from_user.id  # xranim id chata shtob razdelit najatiya knopok polozovatelya

    if btn_name[0:4] == 'lang':
        await quick_commands.set_language(btn_name[-2:],user_id)
    # tut mi udalayem iz slovarya po klucu znaceniye esli user najimaet na knopku back
    if btn_name not in ['repeat', 'back', 'main_menu','calc','back_loc'] and btn_name[0:4] != 'lang':
        current_btn[user_id].append(btn_name)

    levels = {

        "0": lang_menu, # otdaem knopki s yazikami
        "1": main_menu_keyboards,  # Otdayem knopku glavnoye menu
        "2": cities,  # Otdaem knopki gorodov
        "3": liguid,  # Otdaem knopki edinic izmereniya
        "4": unit,  # Otdaem knopku naliciye jidkosti v posilke
        "5": user_input,  # Polzovatel vvodit massu
    }
    # vsa magiya proishodit tut peredaem funkcii urovni
    current_level_function = levels[current_level]
    await current_level_function(
        call,
        btn_name=btn_name
    )


# tut mi prinimaem vvod user i vivodim emu cenu. Za rasscet ceni otvecaet funkciya calculator
@dp.message_handler(state=Test.Q1)
async def answer_q1(message: Union[types.Message, types.CallbackQuery], state: FSMContext):
    answer = message.text
    user_id = message.from_user.id
    # menyaem ',' na '.' tak kak polzovatel mojet vmesto '.' postavit ','
    if ',' in answer:
        answer = answer.replace(',', '.')
    # tut idet proverka na vvod polzovatelya, shtob on ne vvodil cisla kotoriye ne podxodyat dlya massi. Esli polzovatel xocet vvesti v kg,
    # to emu mojno vvodit polojitelniye i veshestvenniye cisla no do 30kg. A esli gr to tolko naturalniye i do 30000gr
    if (re.fullmatch(r'^(0|[1-9]\d*)([.,]\d+)?', answer) and (current_btn[user_id][-1] == _('kg')) and (
            float(answer) <= 30) and float(answer) > 0) or (
            re.fullmatch(r"(?<![-.])(0|[1-9]\d*)", answer) and (current_btn[user_id][-1] == _('gr')) and float(
        answer) <= 30000 and float(answer) > 0):


        city = current_btn[user_id][0]  # peremennaya v kotoroy xranitsya gorod kotoriy vibral polzovatel(baku,gence,sumqayit,diger)
        liq_a = current_btn[user_id][1]  # peremennaya v kotoroy xranitsya informaciya ob nalicii jidkosti v posilke(yes,no)
        unit_p = current_btn[user_id][2]  # peremennaya v kotoroy xranitsya edinica izmereniya(kg,gr)

        # prisvaivaem res znaceniye toy funkcii kotoraya sovpadaet s nazvaniem goroda. Eto delaetsya shto ne uvelicivat kod v razi
        if city == _('Baki'):
            res = await calculator.calculator_baku(_('Baku'), liq_a, unit_p, float(answer))
        elif city == _('Sumqayit'):
            res = await calculator.calculator_gence_sumq(_('Sumgait'), liq_a, unit_p, float(answer))
        elif city == _('Gence'):
            res = await calculator.calculator_gence_sumq(_('Ganja'), liq_a, unit_p, float(answer))
        elif city == _('Diger'):
            res = await calculator.calculator_diqer(_('Other'), liq_a, unit_p, float(answer))
        markup = await kb.repeat_or_main_menu()
        await message.answer(res, reply_markup=markup)
        await state.finish()

    # esli polzovatel nepravilno vvel to opyat vizivaem mashinu sostoyaniy
    else:
        await message.answer(_("You enter the wrong mass. Please enter the right mass"))
        await Test.Q1.set()
