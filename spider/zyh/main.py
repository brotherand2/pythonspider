#coding: utf-8
from scrapy.cmdline import execute
import  os
import urllib
import  requests
import  bs4
def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print ('%.2f%%' % per)
url = 'https://files.yande.re/sample/2223967b4aa3a9f43dbc4178d3bbe8ef/yande.re%20385672%20sample%20feet%20pantyhose%20sweater%20tougetsu_hajime.jpg'
local = 'large.jpg'
def getProxy():

    url = 'http://www.xicidaili.com/'
    local = 'yande.html'
    headers = {
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"

    }
    proxies = {"http": "http://115.231.175.68:8081" }
    content=requests.get(url,headers=headers,proxies=proxies).content;
    soup = bs4.BeautifulSoup(content, "html.parser")
    List = soup.findAll('tr')
    i=0;
    #print(content)
    for item in List:
        Th=item.findAll('td')
        #ip=Th[2]
        if len(Th)>0:
         print("ip is:"+Th[1].text)
urllib.request.urlretrieve(url, local, cbk)
if __name__ == '__main__':
    project_name = "zyh"
    spider_name = "test"

    s = "scrapy crawl test"
    # s = "scrapy crawl %s -o %s -t json" % (spider_name, results_name)
    #execute(s.split())
