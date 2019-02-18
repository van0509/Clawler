# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.http import Request


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        '''
        1.获取文章列表页的url交给scrapy下载后并进行解析
        2.获取下一页的url并交给scrapy进行下载，下载完成后交给parse
        '''

        # 解析列表页中的所有文章中的url并交给scrapy下载后并进行解析
        urls_parrern = r'<a class="archive-title" target="_blank" href="([\s\S]*?)" title="([\s\S]*?)">'

        post_urls = re.findall(urls_parrern, response.text)
        for post_url in post_urls:
            yield Request(url=post_url[0], callback=self.parse_detail)
        # 解析列表中的下一页网址并继续由parse进行解析
        next_pattern = r'<a class="next page-numbers" href="([\s\S]*?)">'
        next_url = re.findall(next_pattern, response.text)
        if next_url:
            yield Request(url=next_url[0], callback=self.parse)

    def parse_detail(self, response):
        title = re.findall(r'<h1>([\s\S]*?)</h1>', response.text)[0]
        creat_date = re.findall('p class="entry-meta-hide-on-mobile">[\s]*?([\S]*?)[\s]&middot;', response.text)[0]
        praise_nums = re.findall(r'votetotal">([\S]*?)</h10> 赞</span>', response.text)[0] + ' 赞'
        fav_nums = re.findall('i class="fa fa-bookmark-o  "></i>([\s\S]*?)</span>', response.text)[0]
        match_re = re.findall('<i class="fa fa-comments-o"></i>([\s\S]*?)</span></a>', response.text)[0]
        pass
