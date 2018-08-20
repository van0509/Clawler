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
import re,multiprocessing
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
    return list(Info)
def parse_Info(url):
    response=requests.get(url,headers=headers).content.decode('gbk')
    pattern='#07519a>([\s\S]*?)</font>[\s\S]*?df["]*?><a href="([\s\S]*?)">'
    infos=re.findall(pattern,response)
    db=myDb.mySql()
    name=infos[0][0]
    link=infos[0][1]
    sql='INSERT INTO seven.movie(name, link)VALUES(%s,%s);'
    params=(name,link)
    resoult=db.execute(sql,params)
    if resoult==True:
        print('Insert 成功')
    else:
        print('Insert 失败')


def spider():
    base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    pool=multiprocessing.Pool(multiprocessing.cpu_count())
    for i in range(1,8):
        url=base_url.format(i)
        moives=get_Info(url)
        # print(moives)
        for m in moives:
            # parse_Info(m)
            pool.apply_async(parse_Info,(m,))
        pool.close()
        pool.join()

if __name__ == '__main__':
    spider()