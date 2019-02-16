# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Dbtest
   Author :       'Seven'
   date：          2019-02-15
-------------------------------------------------
"""
__author__ = 'Seven'
import myDb
from UA import UA
import aiohttp, asyncio, re

db = myDb.mySql()
sql = 'SELECT ID From seven.python;'
resoult = db.readall(sql)
mac = [
    'https://p.bokecc.com/servlet/getvideofile?vid=%s&siteid=0DD1F081022C163E&useragent=Android' % i[0] for i in
    resoult]
headers = {
    'User-agent': UA().userAgent()
}


async def fetch(session, url):
    async with session.get(url, headers=headers) as response:
        return await response.text()


async def parser(html):
    pattern = '"backupurl":"([\s\S]*?)","'
    down = re.findall(pattern, html)
    print(down)


async def down(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        await asyncio.sleep(1)
        await parser(html)


loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(down(u)) for u in mac]
loop.run_until_complete(asyncio.gather(*tasks))
