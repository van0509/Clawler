#!/usr/bin/python3
# coding:utf-8

"""
@author: Seven°
@contact: free001@vip.qq.com
@software: PyCharm
@file: myDb.py
@time: 2018-08-17 23:37
"""
import pymysql


class mySql:
    def __init__(self, host='localhost', port=3306, user='root', passwd='123456', db='seven', charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset

    def connectDateBase(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                                        charset=self.charset)

        except:
            print('conn Error')
            return False
        self.cur = self.conn.cursor()
        return True

    def close(self):
        '''关闭数据库'''

        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True

    def execute(self, sql, params=None):
        if self.connectDateBase() == False:
            return False
        try:
            if self.conn and self.cur:
                self.cur.execute(sql, params)
                self.conn.commit()
        except:
            print('execute' + sql + 'error')
            return False
        return True


if __name__ == "__main__":
    db=mySql()
    sql='INSERT INTO seven.movies(name, link)VALUES(%s,%s);'
    params=("我是谁","www.baidu.com")
    resoult=db.execute(sql,params)
    if resoult==True:
        print('Insert 成功')
    else:
        print('Insert 失败')
