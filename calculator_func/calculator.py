from calculator_func import rate_API
from loader import _

# tekst kotoriy budet vivoditsya posle vvoda massi posilki


async def calculator_baku(city, liq_a, unit, answer):
    text = _("""City: {0}
Liquid in parcel: {1}
Mass: {2} {3}
Price: {4} USD {5} AZN
""")

    x = rate_API.rate
    mass = answer
    if unit == _('gr'):
        answer /= 1000
    if liq_a == _('No'):
        if answer >= 0.001 and answer <= 0.1:
            return text.format(city, liq_a.title(), mass, unit, 0.83, round(0.83 * x, 2))
        elif answer >= 0.101 and answer <= 0.250:
            return text.format(city, liq_a.title(), mass, unit, 1.45, round(1.45 * x, 2))
        elif answer >= 0.251 and answer <= 0.5:
            return text.format(city, liq_a.title(), mass, unit, 2.44, round(2.44 * x, 2))
        elif answer >= 0.501 and answer <= 0.75:
            return text.format(city, liq_a.title(), mass, unit, 2.99, round(2.99 * x, 2))
        elif answer >= 0.751 and answer <= 1:
            return text.format(city, liq_a.title(), mass, unit, 3.49, round(3.49 * x, 2))
        elif answer > 1 and answer <= 10:
            return text.format(city, liq_a.title(), mass, unit, round(3.49 * answer,2), round(3.49 * answer * x, 2))
        elif answer > 10 and answer <= 30:
            return text.format(city, liq_a.title(), mass, unit, round(3.44 * answer, 2), round(3.44 * x * answer, 2))
    if liq_a == _('Yes'):
        if answer >= 0.001 and answer <= 0.1:
            return text.format(city, liq_a.title(), mass, unit, 0.99, round(0.99 * x, 2))
        elif answer >= 0.101 and answer <= 0.250:
            return text.format(city, liq_a.title(), mass, unit, 1.89, round(1.89 * x, 2))
        elif answer >= 0.251 and answer <= 0.500:
            return text.format(city, liq_a.title(), mass, unit, 2.79, round(2.79 * x, 2))
        elif answer >= 0.501 and answer <= 0.750:
            return text.format(city, liq_a.title(), mass, unit, 3.33, round(3.33 * x, 2))
        elif answer >= 0.751 and answer <= 1:
            return text.format(city, liq_a.title(), mass, unit, 3.79, round(3.79 * x, 2))
        elif answer > 1 and answer <= 10:
            return text.format(city, liq_a.title(), mass, unit, round(3.79 * answer, 2), round(3.79 * answer * x, 2))
        elif answer > 10 and answer <= 30:
            return text.format(city, liq_a.title(), mass, unit, round(3.49 * answer, 2), round(3.49 * answer * x, 2))


async def calculator_gence_sumq(city, liq_a, unit, answer):
    text = _("""City: {0}
Liquid in parcel: {1}
Mass: {2} {3}
Price: {4} USD {5} AZN
""")
    x = rate_API.rate
    mass = answer
    if unit == _('gr'):
        answer /= 1000

    if answer >= 0.001 and answer <= 0.250:
        return text.format(city, liq_a.title(), mass, unit, 2.5, round(2.5 * x, 2))
    elif answer >= 0.251 and answer <= 0.500:
        return text.format(city, liq_a.title(), mass, unit, 2.99, round(2.99 * x, 2))
    elif answer >= 0.501 and answer <= 0.700:
        return text.format(city, liq_a.title(), mass, unit, 3.44, round(3.44 * x, 2))
    elif answer >= 0.701 and answer <= 1:
        return text.format(city, liq_a.title(), mass, unit, 3.89, round(3.89 * x, 2))
    elif answer > 1 and answer <= 3:
        return text.format(city, liq_a.title(), mass, unit, round(3.88 * answer, 2), round(3.88 * answer * x, 2))
    elif answer > 3 and answer <= 10:
        return text.format(city, liq_a.title(), mass, unit, round(3.83 * answer, 2), round(3.83 * answer * x, 2))
    elif answer > 10 and answer <= 30:
        return text.format(city, liq_a.title(), mass, unit, round(3.79 * answer, 2), round(3.79 * answer * x, 2))


async def calculator_diqer(city, liq_a, unit, answer):
    text = _("""City: {0}
Liquid in parcel: {1}
Mass: {2} {3}
Price: {4} USD {5} AZN
""")
    x = rate_API.rate
    mass = answer
    if unit == _('gr'):
        answer /= 1000
    if liq_a == _('No'):
        if answer >= 0.001 and answer <= 0.250:
            return text.format(city, liq_a.title(), mass, unit, 2.5, round(2.5 * x, 2))
        elif answer >= 0.251 and answer <= 0.5:
            return text.format(city, liq_a.title(), mass, unit, 3.5, round(3.5 * x, 2))
        elif answer >= 0.501 and answer <= 0.700:
            return text.format(city, liq_a.title(), mass, unit, 3.99, round(3.99 * x, 2))
        elif answer >= 0.701 and answer <= 1:
            return text.format(city, liq_a.title(), mass, unit, 4.99, round(4.99 * x, 2))
        elif answer > 1 and answer <= 3:
            return text.format(city, liq_a.title(), mass, unit, round(4.99 * answer, 2), round(4.99 * answer * x, 2))
        elif answer > 3 and answer <= 30:
            return text.format(city, liq_a.title(), mass, unit, round(4.44 * answer, 2), round(4.44 * x * answer, 2))
    if liq_a == _('Yes'):
        if answer >= 0.001 and answer <= 0.250:
            return text.format(city, liq_a.title(), mass, unit, 2.5, round(2.5 * x, 2))
        elif answer >= 0.251 and answer <= 0.500:
            return text.format(city, liq_a.title(), mass, unit, 3.5, round(3.5 * x, 2))
        elif answer >= 0.501 and answer <= 0.700:
            return text.format(city, liq_a.title(), mass, unit, 3.99, round(3.99 * x, 2))
        elif answer >= 0.701 and answer <= 1:
            return text.format(city, liq_a.title(), mass, unit, 4.99, round(4.99 * x, 2))
        elif answer > 1 and answer <= 3:
            return text.format(city, liq_a.title(), mass, unit, round(4.99 * answer, 2), round(4.99 * answer * x, 2))
        elif answer > 3 and answer <= 30:
            return text.format(city, liq_a.title(), mass, unit, round(4.44 * answer, 2), round(4.44 * answer * x, 2))
