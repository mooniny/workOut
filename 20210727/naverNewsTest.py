# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

cCode = '005930'    #삼성전자

con = HTTPSConnection("finance.naver.com")
link = []
datas = []
article = []
title = []
info = []
date = []
for page in range(1, 3):
    con.request("GET", "/item/news_news.nhn?code=%s&page=%d" % (cCode, page))
    rb = con.getresponse().read()
    ssNewsData = BeautifulSoup(rb, "html.parser", from_encoding = "utf-8")
    ssNewsDatas = ssNewsData.select("tbody tr")
    # print(ssNewsDatas)
    for n in ssNewsDatas:
        # print(n.select("a")[0].attrs["href"])   # 링크
        link.append(n.select("a")[0].attrs["href"])
        for t in n.select(".title"):   # 제목
            # print(t.select('a')[0].text)
            title.append(t.select('a')[0].text)
        for i in n.select(".info"):    # 신문사
            # print(i.text)
            info.append(i.text)
        for d in n.select(".date"):   # 날짜
            # print(d.text)
            date.append(d.text)
        # print("------")
        
        
        con2 = HTTPSConnection("finance.naver.com")         # 기사 전문
        con2.request("GET", n.select("a")[0].attrs["href"])
        rb2 = con2.getresponse().read()
        ssNewsLink = BeautifulSoup(rb2, "html.parser", from_encoding = "utf-8")
        ssNewsLinks = ssNewsLink.select("#news_read")   # article3.xml
        print(ssNewsLinks)
        # for l in ssNewsLinks:
            # print(l.text.strip())
            # print('-------')
            # article.append(l.text.strip())
            # break
            
    # for txt in data:
        # if txt != None and txt != "" and not txt.startswith("관련뉴스") and not txt.startswith('연관기사'):
            # txt = txt.replace('/n',' ').split('\n')
            # datas.append(txt)
            #
# print(link)
# print(article)