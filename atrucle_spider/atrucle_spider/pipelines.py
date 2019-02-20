# -*- coding: utf-8 -*-

import codecs
import json

import MySQLdb
from scrapy.exporters import JsonItemExporter
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline


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
        self.conn = MySQLdb.Connect('localhost', 'root', '123456', 'seven', charset='utf8',use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = '''
        insert into seven.jobbole(title,url,url_object_id,creat_date,front_image_url,front_image_path,fav_nums,comment_nums,praise_nums) values(%s,%s,%s,%s,%s,%s,%s,%s) 
        '''
        self.cursor.execute(insert_sql, (
        item['title'], item['url'], item['url_object_id'], item['creat_date'], item['front_image_url'],
        item['front_image_path'], item['fav_nums'], item['comment_nums'], item['praise_nums']))
        self.conn.commit()


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value['path']
        item['front_image_path'] = image_file_path
        return item
