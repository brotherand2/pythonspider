# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    querystring = u"清华"
    start_urls = []
    for i in range(1, 2, 1):
        start_urls.append("http://weixin.sogou.com/weixin?type=%d&query=%s&page=%d" % (2, querystring, i))



    #def parse(self, response):
       # print ("hello world")
      #  pass



    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="txt-box"]/h3/a')
        for site in sites:
            item = WechatprojectItem()
            item["title"] = site.xpath("text()").extract()  # 其中在item.py中定义了title = Field()
            item["link"] = site.xpath("@href").extract()  # 其中在item.py中定义了link = Field()
            #############################################################################################
            # yield item ## 只抓取当前页数据
            next_url = item["link"][0]
            # yield Request(url=next_url, callback=self.parse2) ## 只抓取二级页面数据
            yield Request(url=next_url, meta={"item": item}, callback=self.parse2)  ## 抓取当前页数和二级页面数据
        pass
    def parse2(self, response):
        soup = BeautifulSoup(response.body)
        tag = soup.find("div", attrs={"class":"rich_media_content", "id":"js_content"}) # 提取第一个标签
        content_list = [tag_i.text for tag_i in tag.findAll("p")]
        content = "".join(content_list)
        # print content
        # item = WechatprojectItem() ## 只抓取二级页面数据
        item = response.meta['item'] ## 抓取当前页数和二级页面数据
        item["content"] = content
        return item
