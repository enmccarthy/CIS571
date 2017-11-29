#import urllib2
import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
from PyQt5.QtWebKit import *  
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWidgets import QApplication
#Take this class for granted.Just use result of rendering.
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

 

def readPage(url, filename):
    ##page = urllib2.urlopen(url)
    r = Render(url)  
    result = r.frame.toHtml()
    #page = requests.get(url)
    ##page_content = page.read()
    differentChars = result.text.encode('utf-8').decode('ascii','ignore')
    soup = BeautifulSoup(differentChars, 'lxml-xml')
    print soup.prettify()
    f = open("./data/"+filename, 'w+')
    #print(soup.get_text())
    f.write(soup.get_text())
    f.close()


readPage(sys.argv[1], sys.argv[2])
