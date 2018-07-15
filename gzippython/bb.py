import urllib.request
import lxml
from bs4 import BeautifulSoup
import  gzip
#url='http://news.sina.com.cn/c/nd/2017-02-05/doc-ifyafcyw0237672.shtml'
#url = 'https://nyaa.si/'
url = 'http://www.pniao.com/Mov'
req = urllib.request.Request(url)

req.add_header('User-Agent',

               'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0')

page = urllib.request.urlopen(req)  # 模仿浏览器登录

txt = page.read()
txt=gzip.decompress(txt).decode('utf-8')

#soup = BeautifulSoup(txt, 'lxml')

#title =soup.select('#artibodyTitle')[0].text
#title = soup.title
#print(title)

print(txt)
