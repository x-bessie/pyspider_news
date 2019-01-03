#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-01-02 11:38:46
# Project: Newsapi
#爬取模板
from pyspider.libs.base_handler import *
import re
import json
from pyspider.result import ResultWorker
import pymysql
import time
import datetime
class Handler(BaseHandler):
    crawl_config = {
    }
    
    #链接数据库
    def __init__(self):
        self.db=pymysql.connect('localhost','root','123456','news',charset='utf8')
    
    def add_Mysql(self,author,title,url,publishedAt,AddOn):
        try:
            cursor=self.db.cursor() 
            sql = 'insert into topnews(author, title, url, publishedAt,AddOn) values ("%s","%s","%s","%s","%s")' % (author, title, url, publishedAt, AddOn);
            print(sql)
            cursor.execute(sql)
            print(cursor.lastrowid)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback() 

    @every(minutes=24 * 60)
    def on_start(self):
        #加上申请的apikey才可用
        self.crawl('https://newsapi.org/v2/top-headlines?country=cn&apiKey=', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):  
        json_result=response.json['articles']
        
        for x in json_result:
            author=x['author'],
            title=x['title'],
            url=x['url'],
            publishedAt=x['publishedAt']
            AddOn=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())            
            #print('{} {} {} {} {}\n'.format(author,title,url,publishedAt,AddOn))
            self.add_Mysql(author,title,url,publishedAt,AddOn)
                   
