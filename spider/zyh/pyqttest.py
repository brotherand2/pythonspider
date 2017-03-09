import sys, re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

p = re.compile(r'<a class="J_AtpLog" href="(.*)" title')

fp = open('deatailUrl.txt', 'a+')


class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()


if __name__ == '__main__':

    r = Render(sys.argv[1])
    ##  r = Render(r'http://list.taobao.com/itemlist/default.htm?spm=a2106.2206569.0.0.Ou8oRH&cat=51108009')
    html = r.frame.toHtml()
    result = p.findall(html)
    i = 0
    for uri in result:
        i += 1
        print(uri, file=fp)
##  print(i)
fp.close()