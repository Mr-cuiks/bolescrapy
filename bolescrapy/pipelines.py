# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy.pipelines.files import FilesPipeline


import MySQLdb


class BolescrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='cui123', db='bole', charset='utf8',
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = '''insert into bolearticle(title,tag,par_num,creat_date,fav_num,article,comment_num) values (%s,%s,%s,%s,%s,%s,%s)'''
        self.cursor.execute(insert_sql,(item['title'], item['tag'],item['par_num'], item['creat_date'], item['fav_num'], item['article'],item['comment_num']))
        self.conn.commit()

# class Items(FilesPipeline):
#     def process_item(self, item, spider):
#         MEDIA_NAME = 'image'
#         return item
