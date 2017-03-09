#coding:utf-8
import requests
import  urllib2
import  urllib
import  httplib
import  cookielib
import  re


r="hello";
#print("my name is"+r)
def testRequest():
    url = "http://www.baidu.com"
    response = requests.get(url)
    content = requests.get(url).content

    print  content
    return
def testGet(url):
    z_request=urllib2.Request(url)
    #print  z_request

    response=urllib2.urlopen(z_request)
    #resquest_data=response.read()
    print  response.read()
    return ;

def testHttpGet(url):
    conn=httplib.HTTPConnection(url)
    conn.request(method="get",url=url)
    response=conn.getresponse()
    print  response.read()
#testRequest();
#testGet("https://api.tuxiaobei.com/story/video-types")
def testPost():
    cookiestr = 'gkr8_2132_saltkey=8gr4YzYy; gkr8_2132_auth=ee5co0gnXEcCChRjWolv5HiUKqb9uJ%2FseQDYzVrCp7Jy5xqzPnOqerJXAUDSJdlly9x2XU3km0F%2BH7cY%2F0wvLCbUtA0 ';

    headers={
        "User-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer":"http://www.tsdm.me/home.php?mod=space&do=notice&isread=1",
        "Cookie":cookiestr
    }
    loginurl = 'http://www.tsdm.me/plugin.php?id=dsu_paulsign:sign&21ddc11c&infloat=yes&handlekey=dsu_paulsign&inajax=1&ajaxtarget=fwin_content_dsu_paulsign';
    signurl = 'http://www.tsdm.me/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1&inajax=1';
    request=urllib2.Request(loginurl,None,headers)


    conn= urllib2.urlopen(request)
    response=conn.read()
    searchobj=re.search(r"<input type=\"hidden\" name=\"formhash\" value=\"(.*)\">",response)

    print "hash is:"+searchobj.group(1)

    if (searchobj.group(1)):
         data={
             "qdxq":"wl",
             "qdmode":"1",
             "todaysay":"签到了aaa",
              "fastreply":"1",
             "formhash":searchobj.group(1)
         }
    postdata = urllib.urlencode(data)
    request2 = urllib2.Request(signurl, postdata, headers)
    conn = urllib2.urlopen(request2)
    response = conn.read()
    print  response
    return
#testHttpGet("https://api.tuxiaobei.com/story/videos")
#testPost()


