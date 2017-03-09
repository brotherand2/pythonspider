import urllib.request
import  requests
import  bs4

proxies=[]


def get(url: str, header: list = {}):
    """
    HTTP GET获取
    :param url: URL地址
    :param header: HTTP头
    :return: row
    """
    header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    header['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2883.103 Safari/537.36'
    content=requests.get(url,headers=header).content;
    #req = urllib.request.Request(url, headers=header)
    #return urllib.request.urlopen(req).read()
    return content

def getProxyIps():
    url = 'http://www.xicidaili.com/'
    headers = {
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"

    }
    content = requests.get(url, headers=headers).content;
    soup = bs4.BeautifulSoup(content, "html.parser")
    List = soup.findAll('tr')
    i = 0;

    # print(content)
    for item in List:
        Th = item.findAll('td')
        # ip=Th[2]
        if len(Th) > 0:
            proxies.append(Th[1].text)
    return  proxies