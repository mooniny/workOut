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
        # print("-------------------------------------------")
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
        
        ssNewsLink = ssNewsLink.select("#news_read")
        # ssNewsLink = ssNewsLink.select("div.scr01")
        # print(ssNewsLink)
        
        ep = None
        ep2 = None
        ep3 = None
        for l in ssNewsLink:
            ssNews = l.text.strip()
            if l.select("strong.media_end_summary"):
                ep = l.select("strong.media_end_summary")[0].text
                # ssNews = l.text.replace(ep, "")
                ssNews = ssNews.strip(ep)
                
            elif l.select("span.end_photo_org"):
                ep2 = l.select("span.end_photo_org")[0].text
                # ssNews = l.text.replace(ep2, "")
                ssNews = ssNews.strip(ep2)
                
            elif l.select("div.link_news"):
                ep3 = l.select("div.link_news")[0].text
                # ssNews = l.text.replace(ep3, "")
                ssNews = ssNews.strip(ep3)
            
            print(ssNews)
            
            
print(link)