# -*- coding: utf-8 -*-
# @Author  : Seven°
# @Email   : free001@vip.qq.com
# @Software: PyCharm
# @File    : re_demo.py
# @Time    : 2018-08-22 23:57
import requests,re
from UA import UA
def parse_page(url):
    headers={
        'User-agent':UA().userAgent()
    }

    response = requests.get(url, headers).text
    pattern = r'.aspx">([\s\S]*?)</a>[\s\S]*?.aspx">([\s\S]*?)</a>'
    resp = re.findall(pattern, response)
    for i in resp:
        Info=i[0]+'--'+i[1]
        print(Info)


def main():
    url = 'https://so.gushiwen.org/mingju/default.aspx?p=%s&c=&t='
    for i in range(1, 200):
        url1 = url % i
        parse_page(url1)
if __name__ == '__main__':
    main()