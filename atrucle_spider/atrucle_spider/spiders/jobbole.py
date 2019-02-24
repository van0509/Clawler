# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.http import Request

from ..items import JobBoleArticleItem
from ..utils.common import get_md5


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
        urls_parrern = r'<a target="_blank" href="([\S]*?)" title="([\s\S]*?)"><img src="([\S]*?)" alt="" width="120" height="120" /></a>'
        post_urls = re.findall(urls_parrern, response.text)
        for post_url in post_urls:
            yield Request(url=post_url[0], meta={'front_image_url': post_url[2]}, callback=self.parse_detail)
        # 解析列表中的下一页网址并继续由parse进行解析
        next_pattern = r'<a class="next page-numbers" href="([\s\S]*?)">'
        next_url = re.findall(next_pattern, response.text)
        if next_url:
            yield Request(url=next_url[0], callback=self.parse)

    def parse_detail(self, response):
        article_item=JobBoleArticleItem()
        front_image_url = response.meta.get('front_image_url', )  # 文章封面图
        title = re.findall(r'<h1>([\s\S]*?)</h1>', response.text)[0]
        creat_date = re.findall('p class="entry-meta-hide-on-mobile">[\s]*?([\S]*?)[\s]&middot;', response.text)[0]
        praise_nums = re.findall(r'votetotal">([\S]*?)</h10> 赞</span>', response.text)[0] + '赞'
        fav_nums = re.findall('i class="fa fa-bookmark-o  "></i>([\s\S]*?)</span>', response.text)[0]
        comment_nums = re.findall('<i class="fa fa-comments-o"></i>([\s\S]*?)</span></a>', response.text)[0]
        article_item['title']=title
        article_item['url']=response.url
        article_item['url_object_id']=get_md5(response.url)
        article_item['front_image_url']=[front_image_url]
        # try:
        #     creat_dates=datetime.datetime.strptime(creat_date,'%Y/%M/%D').date()
        # except Exception as e:
        #     creat_dates=datetime.datetime.now().date()
        article_item['creat_date']=creat_date
        article_item['fav_nums']=fav_nums
        article_item['praise_nums']=praise_nums
        article_item['comment_nums']=comment_nums

        yield article_item

        pass
