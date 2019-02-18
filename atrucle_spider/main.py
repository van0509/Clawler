# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Author :       'Seven'
   date：          2019-02-18
-------------------------------------------------
"""
__author__ = 'Seven'

import os
import sys

from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'jobbole'])
