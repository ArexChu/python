# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

'''
Scrapy爬虫作业：

爬取http://futures.eastmoney.com/a/ainesc_1.html网站数据

爬取字段：标题，新闻url，时间3个字段保存到mysql,

标题，新闻url,新闻正文保存到mongdb

要求：1、使用scrapy框架爬取

2、需要用到两个pipeline （先保存到mysql再保存到mongdb）
'''

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
import pymysql
import pymongo

class CleanData:
    def process_item(self, item, spider):
        item['text'] = re.sub('\s+', '', ''.join(item['text']))
        return item
class WriteDataMysql:
    def __init__(self):
        self.connect = self.connect_db()
        self.create_table()
    def process_item(self, item, spider):
        #print("item:{},{},{}".format(item['name'],item['url'],item['date']))
        self.insert_data(item)
        return item
    def connect_db(self):
        connect = pymysql.connect(host='10.91.202.131',
                             user='ow_ai',
                             password='test',
                             database='ai')
        return connect
    def create_table(self):
        cursor = self.connect.cursor()
        create_table = "create table if not exists news(name varchar(500), url varchar(500), date varchar(500))"
        cursor.execute(create_table)
    def insert_data(self, item):
        insert_data = "insert into news values('{}','{}','{}');".format(item['name'],item['url'],item['date'])
        #print(insert_data)
        cursor = self.connect.cursor()
        cursor.execute(insert_data)
        self.connect.commit()
    def close_db(self):
        self.connect.close()

class WriteDataMongo:
    def __init__(self):
        self.connect = pymongo.MongoClient('10.91.196.10',
                                      username='ow_ai',
                                      password='test')
        self.db = self.connect["ai"]
        self.collection = self.db["news"]
        
    def process_item(self, item, spider):
        #print("process_item:%s"%item['text'])
        news = {"name":item['name'], "url":item['url'], "text":item['text']}
        self.collection.insert(news)
