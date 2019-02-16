# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     kuai proixe
   Author :       'Seven'
   date：          2019-02-16
-------------------------------------------------
"""
__author__ = 'Seven'
import json
# import aiohttp, asyncio,re
#
# urls = ['https://www.kuaidaili.com/free/inha/%d/' % i for i in range(1, 5)]
#
#
# async def down(url):
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session,url)
#         await parser(html)
#
# async def fetch(session,url):
#     async with session.get(url) as response:
#         return  await response.text(encoding='utf8')
#
# async def parser(html):
#     pattern=r'"IP">([\S]*?)</td>[\s\S]*?"PORT">([\S]*?)</td>'
#     resp=re.findall(pattern,html)
#     proixe=['%s:%s'%(ip,port) for ip,port in resp]
#     print(proixe)
#
# loop=asyncio.get_event_loop()
# tasks=[asyncio.ensure_future(down(url))for url in urls]
# tasks=asyncio.gather(*tasks)
# loop.run_until_complete(tasks)

text={"uid":"0DD1F081022C163E","img":"http://2-img.bokecc.com/comimage/0DD1F081022C163E/2018-07-05/17BBADBC3CB2A60F9C33DC5901307461-1.jpg","UPID":"1541211550299182913","vrmode":0,"copies":[{"playurl":"http://cd12-c120.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/17BBADBC3CB2A60F9C33DC5901307461-20.m3u8?t=1550306382&key=29A7259D266BF2DDE43E2AF560454FA7&tpl=10&tpt=112","mediatype":1,"backupurl":"http://cd15-c120-1.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/17BBADBC3CB2A60F9C33DC5901307461-20.m3u8?t=1550306382&key=29A7259D266BF2DDE43E2AF560454FA7&tpl=10&tpt=112","desp":"高清","quality":20},{"playurl":"http://cd12-c120.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/17BBADBC3CB2A60F9C33DC5901307461-10.m3u8?t=1550306382&key=165942F6C1228EE234F40986EF86ECD7&tpl=10&tpt=112","mediatype":1,"backupurl":"http://cd15-c120-1.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/17BBADBC3CB2A60F9C33DC5901307461-10.m3u8?t=1550306382&key=165942F6C1228EE234F40986EF86ECD7&tpl=10&tpt=112","desp":"清晰","quality":10}],"playtype":0,"authenable":1,"freetime":0,"defaultquality":10,"vid":"17BBADBC3CB2A60F9C33DC5901307461","status":1}

a=json.loads('{"uid":"0DD1F081022C163E","img":"http://2-img.bokecc.com/comimage/0DD1F081022C163E/2018-07-05/17BBADBC3CB2A60F9C33DC5901307461-1.jpg","UPID":"1541211550299182913","vrmode":0,"copies":[{"playurl":"http://cd12-c120.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/17BBADBC3CB2A60F9C33DC5901307461-20.m3u8?t=1550306382&key=29A7259D266BF2DDE43E2AF560454FA7&tpl=10&tpt=112","mediatype":1,"backupurl":"http://cd15-c120-1.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/17BBADBC3CB2A60F9C33DC5901307461-20.m3u8?t=1550306382&key=29A7259D266BF2DDE43E2AF560454FA7&tpl=10&tpt=112","desp":"高清","quality":20},{"playurl":"http://cd12-c120.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/17BBADBC3CB2A60F9C33DC5901307461-10.m3u8?t=1550306382&key=165942F6C1228EE234F40986EF86ECD7&tpl=10&tpt=112","mediatype":1,"backupurl":"http://cd15-c120-1.play.bokecc.com/flvs/0DD1F081022C163E/2018-07-05/17BBADBC3CB2A60F9C33DC5901307461-10.m3u8?t=1550306382&key=165942F6C1228EE234F40986EF86ECD7&tpl=10&tpt=112","desp":"清晰","quality":10}],"playtype":0,"authenable":1,"freetime":0,"defaultquality":10,"vid":"17BBADBC3CB2A60F9C33DC5901307461","status":1}'
,encoding='utf8')
if a['copies'][0]['desp'] =='高清':
    print(a['copies'][0]['playurl'])