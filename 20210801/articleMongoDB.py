# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from pymongo.mongo_client import MongoClient

cCode = '005930'    #삼성전자
h = {'User-agent' : 'mozilla/5.0'}

conMongo = MongoClient("")
db = conMongo.xe

con = HTTPSConnection("finance.naver.com")
title = []
info = []
date = []
link = []
article = []
for page in range(1, 3):
    con.request("GET", "/item/news_news.nhn?code=%s&page=%d" % (cCode, page), headers = h)
    rb = con.getresponse().read()
    ssNewsData = BeautifulSoup(rb, "html.parser", from_encoding = "utf-8")
    ssNewsDatas = ssNewsData.select("tbody tr")
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
        
        
        con2 = HTTPSConnection("finance.naver.com")         # 기사 전문
        con2.request("GET", n.select("a")[0].attrs["href"], headers = h)
        rb2 = con2.getresponse().read()
        # print(rb2)
        ssNewsLink = BeautifulSoup(rb2, "html.parser", from_encoding = "euc-kr")
        # print(ssNewsLink)
        ssNewsLinks = ssNewsLink.select("#news_read")
        # print(ssNewsLinks)
        for l in ssNewsLinks:
            # del l.select(".end_photo_org")
            # print(l)
            # print(l)
            # print(type(l))
            # print(l.text)
            article.append(l.text.replace(l.select(".link_news")[0].text, "").replace(l.select(".end_photo_org")[0].text, ""))
            # print(l.text.replace(l.select(".link_news")[0].text, "").replace(l.select(".end_photo_org")[0].text, ""))
con2.close() 
con.close()
            
db.news_list.insert({"title":title, "info":info, "date":date, "link":link, "article":article})

result = db.news_list.find()
for c in result:
    print(c["title"], c["info"], c["date"], c["link"])
    print(c["article"])
conMongo.close()
            
            
            
            
            
            