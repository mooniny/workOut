# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from cx_Oracle import connect

cCode = '005930'    #삼성전자
h = {'User-agent' : 'mozilla/5.0'}

con = HTTPSConnection("finance.naver.com")
link = []
datas = []
article = []
title = []
info = []
date = []
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

     
import pandas as pd
            
con = connect("moony/pink88@192.168.0.131:1521/xe")
sql = "select * from kma_weather_moon"
weatherDF = pd.read_sql(sql, con)
con.close()
print(weatherDF)

weatherPT = weatherDF.pivot_table(index='KW_WFKOR', columns='KW_HOUR', values='KW_TEMP')
print(weatherPT)             
            
            
            
            
            
            