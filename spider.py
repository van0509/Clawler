#!/usr/bin/python3
#coding:utf-8

"""
@author: Seven°
@contact: free001@vip.qq.com
@software: PyCharm
@file: spider.py
@time: 2018-08-14 3:50
"""

import requests
import re
import myDb
from UA import UA
# url='http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'
BASE_DOMAN='http://www.ygdy8.net/'
headers={
    'User-Agent': UA().userAgent()
}

def get_Info(url):
    response=requests.get(url,headers=headers,).text
    pattern='<td height="26">[\s\S]*?<a href="([\s\S]*?)" class="ulink">([\s\S]*?)</a>'
    Info=re.findall(pattern,response)
    Info=map(lambda url:BASE_DOMAN+url[0],Info)
    return Info
def parse_Info(url):
    response=requests.get(url,headers=headers).content.decode('gbk')
    pattern='<font color=#07519a>([\s\S]*?)</font>[\s\S]*?"#fdfddf"><a href="([\s\S]*?)">'
    infos=re.findall(pattern,response)
    db=myDb.mySql()
    name=infos[0][0]
    link=infos[0][1]
    sql='INSERT INTO seven.movies(name, link)VALUES(%s,%s);'
    params=(name,link)
    resoult=db.execute(sql,params)
    if resoult==True:
        print('Insert 成功')
    else:
        print('Insert 失败')


def spider():
    base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    for i in range(1,8):
        url=base_url.format(i)
        moives=get_Info(url)
        for m in moives:
            parse_Info(m)

if __name__ == '__main__':

    spider()