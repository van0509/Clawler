# -*- coding: utf-8 -*-

import codecs
import json

import pymysql
from scrapy.exporters import JsonItemExporter
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from twisted.enterprise import adbapi


class AtrucleSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False + '\n')
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class JsonExporterPipeline(object):
    # 调用scrapy提供的json export到处jsonwenjian
    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_sipder(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class MysqlePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', '123456', 'seven', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = '''insert into jobbole(title,url,url_object_id,creat_date,front_image_url,front_image_path,fav_nums,comments_nums,praise_nums) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        params = (item['title'], item['url'], item['url_object_id'], item['creat_date'], item['front_image_url'],
                  item['front_image_path'], item['fav_nums'], item['comment_nums'], item['praise_nums'])
        self.cursor.execute(insert_sql, params)
        self.conn.commit()


class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_setting(cls, settings):
        dbparms = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PWD'],
            charset='utf8',
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twusted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)  # 处理异常
        return item

    def handle_error(self, failure):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 具体的插入操作
        insert_sql = '''insert into jobbole(title,url,url_object_id,creat_date,front_image_url,front_image_path,fav_nums,comments_nums,praise_nums) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        params = (item['title'], item['url'], item['url_object_id'], item['creat_date'], item['front_image_url'],
                  item['front_image_path'], item['fav_nums'], item['comment_nums'], item['praise_nums'])
        cursor.execute(insert_sql, params)


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value['path']
        item['front_image_path'] = image_file_path
        return item
