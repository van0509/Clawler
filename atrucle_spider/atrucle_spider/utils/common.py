# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     common
   Author :       'Seven'
   date：          2019-02-21
-------------------------------------------------
"""
__author__ = 'Seven'

import hashlib
import pymysql


def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

def conn_mysql(conn):

    corsur=conn.cursor()
    print(corsur)

if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='seven', charset='utf8')
    conn_mysql(conn)