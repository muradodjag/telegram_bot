# tut ya ispolzuyu global peremennuyu i poka shto ne znayu kak ee pomenyat na shto to drugoye
# ispolzuem aiohttp tak kak on asinhronniy
# a request_xml dobavili v schedule shtob on kajdiy den obnovlal kurs

import aiohttp
import datetime
from xml.etree import cElementTree

test_date = '05.06.2016'
today = datetime.datetime.today()
rate = 1.7
async def request_xml():
    async with aiohttp.ClientSession() as session:
        rate_url = "https://www.cbar.az/currencies/{}.xml".format(today.strftime("%d.%m.%Y"))
        async with session.get(rate_url) as resp:
            global rate
            response = await resp.content.read()
            tree = cElementTree.fromstring(response)
            rate = float(tree[1][0][2].text)







