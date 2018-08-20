# -*- coding:utf-8 -*-
'''
@project=Clawler
@file=dytt
@Author=Administrator
@creat_time=2018/8/2019:02
'''
from UA import UA
from myDb import mySql
from lxml import etree
import requests,asyncio


BASE_URL='http://www.ygdy8.net'
headers={
    'User-Agent':UA().userAgent()
}
def get_detail_urls(url):
    respone = requests.get(url, headers=headers).text
    html = etree.HTML(respone)
    deatail_ursl = html.xpath("//table[@class='tbspan']//a/@href")
    Info = map(lambda urls: BASE_URL + urls, deatail_ursl)
    return Info

def parse_info(info,rule):
    return info.replace(rule,'').strip()

def parse_detail_page(url):
    movie={}
    response=requests.get(url,headers=headers).content.decode('gbk')
    html=etree.HTML(response)
    movie['title']=html.xpath("//div//font[@color='#07519a']/text()")[0]
    zoomE=html.xpath("//div[@id='Zoom']")[0]
    imgs=zoomE.xpath(".//img/@src")
    movie['cover']=imgs[0]
    # movie['screenshot']=imgs[1]
    Infos=zoomE.xpath('.//text()')
    for index,info in enumerate(Infos):
        if info.startswith('◎年　　代'):
            info=parse_info(info,'◎年　　代')
            movie['year']=info
        elif info.startswith('◎产　　地'):
            info = parse_info(info, '◎产　　地')
            movie['country']=info
        elif info.startswith('◎类　　别'):
            info = parse_info(info, '◎类　　别')
            movie['category']=info
        elif info.startswith('◎豆瓣评分'):
            info = parse_info(info, '◎豆瓣评分')
            movie['douban_rating']=info
        elif info.startswith('◎片　　长'):
            info = parse_info(info, '◎片　　长')
            movie['duration']=info
        elif info.startswith('◎导　　演'):
            info = parse_info(info, '◎导　　演')
            movie['director']=info
        elif info.startswith('◎主　　演'):
            info = parse_info(info, '◎主　　演')
            actors=[info]
            for x in range(index+1,len(Infos)):
                actor=Infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors']=info
        elif info.startswith('◎简　　介'):
            info = parse_info(info, '◎简　　介')
            for x in range(index+1,len(Infos)):
                profile=Infos[x].strip()
                if profile.startswith('【下载地址】'):
                    break
            movie['profile']=info
    download_url=html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url']=download_url
    return movie

async def spider():
    base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    for i in range(1,8):
        url=base_url.format(i)
        movie=get_detail_urls(url)
        for x in movie:
            info=parse_detail_page(x)
            print(info)

if __name__ == '__main__':
    tasks=[asyncio.ensure_future(spider())]
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))