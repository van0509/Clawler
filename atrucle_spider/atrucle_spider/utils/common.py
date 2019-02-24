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


def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()