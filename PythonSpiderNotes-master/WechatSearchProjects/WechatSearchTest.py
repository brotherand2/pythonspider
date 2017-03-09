#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  os
import sys
import re
import urllib, urllib2
import requests
import pymongo
import datetime
from bs4 import BeautifulSoup
import multiprocessing as mp

querystring = u" 程序员"
class MongoDBIO:
    # 申明相关的属性
    def __init__(self, host, port, name, password, database, collection):
        self.host = host
        self.port = port
        self.name = name
        self.password = password
        self.database = database
        self.collection = collection

    # 连接数据库，db和posts为数据库和集合的游标
    def Connection(self):
        # connection = pymongo.Connection() # 连接本地数据库
        connection = pymongo.Connection(host=self.host, port=self.port)
        # db = connection.datas
        db = connection[self.database]
        if self.name or self.password:
            db.authenticate(name=self.name, password=self.password) # 验证用户名密码
        # print "Database:", db.name
        # posts = db.cn_live_news
        posts = db[self.collection]
        # print "Collection:", posts.name
        return posts

# # 保存操作
# def ResultSave(save_host, save_port, save_name, save_password, save_database, save_collection, save_contents):
#     posts = MongoDBIO(save_host, save_port, save_name, save_password, save_database, save_collection).Connection()
#
#     for save_content in save_contents:
#         posts.save(save_content)
# 保存操作
def ResultSave(save_host, save_port, save_name, save_password, save_database, save_collection, save_content):
    posts = MongoDBIO(save_host, save_port, save_name, save_password, save_database, save_collection).Connection()
    posts.save(save_content)


def GetTitleUrl(url, data):
    headers = {
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Referer": "http://weixin.sogou.com/weixin?query=%E7%A8%8B%E5%BA%8F%E5%91%98&type=2&page=2&ie=utf8",
        "Cookie": "CXID=47D74AB0C3608336BCA7EF82FF4EE8A9; ABTEST=0|1488613838|v1; IPLOC=CN4414; SUID=A98A84DB721A910A0000000058BA71CE; PHPSESSID=1t0l1q9e89cuq38na0e8gv9vi0; SUIR=1488613838; SUID=A98A84DB3220910A0000000058BA71CF; SUV=00CE177FDB848AA958BA71D17C061503; SNUID=02202E70ABAFE249466E85A7ABDA9B25; JSESSIONID=aaa7XAf0_vZQYgqD8roQv"
    }
    content = requests.get(url=url, data=data,headers=headers).content # GET请求发送
    soup = BeautifulSoup(content)
    tags = soup.findAll("h3")
    titleurl = []
    for tag in tags:
        item = {"title":tag.text.strip(), "link":tag.find("a").get("href"), "content":""}
        titleurl.append(item)
    return titleurl

def GetContent(url):
    soup = BeautifulSoup(requests.get(url=url).content)
    tag = soup.find("div", attrs={"class":"rich_media_content", "id":"js_content"}) # 提取第一个标签
    content_list = [tag_i.text for tag_i in tag.findAll("p")]
    content = "".join(content_list)
    return content

def ContentSave(item):
    # 保存配置
    save_host = "localhost"
    save_port = 27017
    save_name = ""
    save_password = ""
    save_database = "testwechat"
    save_collection = "result"

    save_content = {
        "title":item["title"],
        "link":item["link"],
        "content":item["content"]
    }

    ResultSave(save_host, save_port, save_name, save_password, save_database, save_collection, save_content)

def func(tuple):
    querystring, type, page = tuple[0], tuple[1], tuple[2]
    url = "http://weixin.sogou.com/weixin"
    # get参数
    data = {
        "query":querystring,
        "type":type,
        "page":page
    }

    titleurl = GetTitleUrl(url, data)

    for item in titleurl:
        url = item["link"]
        print "url:", url
        content = GetContent(url)
        item["content"] = content


        StringListSave( querystring, item["title"], content)
        #ContentSave(item)

def StringListSave(save_path, filename, content):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path+"/"+filename+".txt"
    with open(path, "w+") as fp:

            fp.write("%s " % (content.encode("utf8")))
if __name__ == '__main__':
    start = datetime.datetime.now()


    type = 2 # 2-文章，1-微信号

    # 多进程抓取
    p = mp.Pool()
    p.map_async(func, [(querystring, type, page) for page in range(1, 50, 1)])
    p.close()
    p.join()

    # # 单进程抓取
    # for page in range(1, 50, 1):
    #     tuple = (querystring, type, page)
    #     func(tuple)

    end = datetime.datetime.now()
    print "last time: ", end-start
