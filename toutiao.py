#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-01-03 19:51:51
# Project: juhe_toutiao
#juhe
from pyspider.libs.base_handler import *
import pymysql
import time
import datetime
class Handler(BaseHandler):
    crawl_config = {
    }
    
    #数据库设置
    def __init__(self):
        self.db=pymysql.connect('localhost','root','123456','news',charset='utf8')
    #插入数据库
    def add_Mysql(self,author_name,title,date,url,AddOn,category):
        try:
            cursor=self.db.cursor() 
            #sql = 'insert into juhe(author_name, title,date,url,AddOn,category) values ("%s","%s","%s","%s","%s","%s")' % (author_name, title, date, url, AddOn,category);
            #print(sql)
            cursor.execute("insert into juhe(author_name, title,date,url,AddOn,category) values (%s,%s,%s,%s,%s,%s)",(str(author_name),str(title),str(date),str(url),str(AddOn),str(category)))
            #print(cursor.lastrowid)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback() 
    
    
    @every(minutes=24 * 60)
    def on_start(self):
        #加上key才可以用
        self.crawl('http://v.juhe.cn/toutiao/index?key=', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):  
        json_result=response.json["result"]["data"]
        #print(json_result)
        #print(len(response.json["result"]["data"]))
        for i in range(len(response.json["result"]["data"])):
            dict=response.json["result"]["data"][i]
            
            author_name=dict["author_name"]
            title=dict["title"]
            date=dict["date"]
            url=dict["url"]
            AddOn=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            category=dict["category"]                                               
            print('{} {} {} {} {}\n'.format(author_name,title,date,url,AddOn,category)) #这个可以检查你爬取的内容
            #插入数据库
            self.add_Mysql(author_name,title,date,url,AddOn,category)
    