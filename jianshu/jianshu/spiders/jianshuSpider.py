#coding=utf-8
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from jianshu.items import JianshuItem
import urllib


class Jianshu(CrawlSpider):
    name='jianshu'
    start_urls=['http://www.jianshu.com/trending/monthly']
    page=1
    url='http://www.jianshu.com/trending/monthly'
    def parse(self, response):
        item = JianshuItem()
        selector = Selector(response)
        articles = selector.xpath('//ul[@class="note-list"]/li')

        for article in articles:
            title = article.xpath('div/a/text()').extract()
            url = article.xpath('div/a/@href').extract()
            author = article.xpath('div/div[1]/div/a/text()').extract()

            # 下载所有热门文章的缩略图, 注意有些文章没有图片
            try:#/div/div[1]/a/img
                image = article.xpath("div/div[1]/a/img/@src").extract()[0]
                filename='images/%s-%s.jpg' %(author[0],title[0])
                print("文件名:"+filename)
                print("图片地址"+image)
                urllib.request.urlretrieve(image, filename)
            except:
                print ('--no---image--')

            #//*[@id="note-9417518"]/div/div[2]/a[1],阅读数
            listtop = article.xpath('div/div[2]/a[1]/text()').extract()
            #
            likeNum = article.xpath('div/div[2]/span[1]/text()').extract()
            #//*[@id="note-9417518"]/div/div[2]/a[2]/i
#//*[@id="note-9417518"]/div/div[2]/a[2]
            readAndComment = article.xpath('div/div[2]/a[2]/text()')

            test=readAndComment[1].extract()

            item['title'] = title
            item['url'] = 'http://www.jianshu.com/'+url[0]
            item['author'] = author

            item['readNum']=listtop[1]

            # 有的文章是禁用了评论的
            try:
                item['commentNum']=readAndComment[1].extract()
            except:
                item['commentNum']=''
            item['likeNum']= likeNum
            yield item
#/html/body/div[1]/div/div[1]/a
        #next_link = selector.xpath('//a')
#xpath(‘//div[contains(@id,”ma”)]‘)


        if len(articles) >0 :
            self.page=self.page+1
            next_link = self.url+"?page="+ str(self.page)
            print ("----"+next_link)
            yield Request(next_link,callback=self.parse)


