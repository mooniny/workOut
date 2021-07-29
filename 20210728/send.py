# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

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
        con2.request("GET", n.select("a")[0].attrs["href"])
        rb2 = con2.getresponse().read()
        ssNewsLink = BeautifulSoup(rb2, "html.parser", from_encoding = "utf-8")
        ssNewsLinks = ssNewsLink.select("#news_read")
        # print(ssNewsLinks)
        
        
        # notUse1 = None
        # notUse2 = None
        ineedIt = []
        for l in ssNewsLinks:
            if len(l) > 0:
                # if l.select(".end_photo_org")[0].text != None:
                    pass
            elif len(l) == None:
                pass     
            else:
                print(l.text.replace(l.select(".link_news")[0].text, ""))
                
                
                
            # if l.select('.end_photo_org")[0].text == '...':
    # print(link)
    
    
    
    
    
    
    
    
    