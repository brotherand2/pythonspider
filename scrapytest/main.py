#coding: utf-8
from scrapy.cmdline import execute
import  os
import urllib
import  requests

if __name__ == '__main__':
    project_name = "zyh"
    spider_name = "test"

    s = "scrapy crawl dmoz"
    # s = "scrapy crawl %s -o %s -t json" % (spider_name, results_name)
    execute(s.split())
