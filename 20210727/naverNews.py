# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

cCode = '005930'    #삼성전자

con = HTTPSConnection("finance.naver.com")
link = []
data = []
datas = []
article = []
for page in range(1, 10):
    con.request("GET", "/item/news_news.nhn?code=%s&page=%d" % (cCode, page))
    rb = con.getresponse().read()
    ssNewsData = BeautifulSoup(rb, "html.parser", from_encoding = "utf-8")
    ssNewsDatas = ssNewsData.select("tbody tr")
    # print(ssNewsDatas)
    for n in ssNewsDatas:
        print(n.text.strip())
        link.append(n.select("a")[0].attrs["href"])
        data.append(n.text.strip())
        
        con2 = HTTPSConnection("finance.naver.com")         # 기사 전문
        con2.request("GET", n.select("a")[0].attrs["href"])
        rb2 = con2.getresponse().read()
        ssNewsLink = BeautifulSoup(rb2, "html.parser", from_encoding = "utf-8")
        ssNewsLinks = ssNewsLink.select("#news_read")
        # print(ssNewsLinks)
        # for l in ssNewsLinks:
            # print(l.text.strip())
            # print('-------')
            # article.append(l.text.strip())
            # break
            
    for txt in data:
        if txt != None and txt != "" and not txt.startswith("관련뉴스") and not txt.startswith('연관기사'):
            txt = txt.replace('/n',' ').split('\n')
            datas.append(txt)
            
# print(link)
# print(article)