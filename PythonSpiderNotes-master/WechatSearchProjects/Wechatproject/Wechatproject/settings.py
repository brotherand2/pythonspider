# Scrapy settings for Wechatproject project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#



#BOT_NAME = 'Wechatproject'

SPIDER_MODULES = ['Wechatproject.spiders']
NEWSPIDER_MODULE = 'Wechatproject.spiders'
ITEM_PIPELINES = {'Wechatproject.pipelines.WechatprojectPipeline': 1}
DOWNLOAD_DELAY = 1
USER_AGENT='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
DEFAULT_REQUEST_HEADERS = {
    'Cookie':'CXID=47D74AB0C3608336BCA7EF82FF4EE8A9; ABTEST=0|1488613838|v1; IPLOC=CN4414; SUID=A98A84DB721A910A0000000058BA71CE; SUIR=1488613838; SUID=A98A84DB3220910A0000000058BA71CF; SUV=00CE177FDB848AA958BA71D17C061503; SNUID=02202E70ABAFE249466E85A7ABDA9B25; weixinIndexVisited=1; JSESSIONID=aaarVAm3OCdPKgbIcpoQv; sct=1',
    'Referer': 'http://weixin.sogou.com/weixin?query=%E7%A8%8B%E5%BA%8F%E5%91%98&_sug_type_=&s_from=input&_sug_=n&type=2&page=3&ie=utf8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
#ITEM_PIPELINES = ['Wechatproject.pipelines.WechatprojectPipeline'] # add settings
#############################################################################################
# '''if you want to download images'''
# ITEM_PIPELINES = {'Wechatproject.pipelines.WechatprojectPipeline':1, 'Wechatproject.pipelines.MyImagesPipeline':2 # add settings
# IMAGES_STORE = './images'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Wechatproject (+http://www.yourdomain.com)'
