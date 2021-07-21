# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

# https://finance.naver.com/item/news_news.nhn?code=005930&page=2
# https://finance.naver.com/item/news.nhn?code=005930
cCode = '005930'    #삼성전자

con = HTTPSConnection("finance.naver.com")
link = []
title = []
press = []
date = []
for page in range(1, 5):
    con.request("GET", "/item/news_news.nhn?code=%s&page=%d" % (cCode, page))
    rb = con.getresponse().read()
    # print(rb.decode())
    ssNewsData = BeautifulSoup(rb, "html.parser", from_encoding = "utf-8")
    ssNewsDatas = ssNewsData.select("tbody tr")
    for n in ssNewsDatas:
        # # print(n.select("a"))
        # # print(type(n.select("a")))
        # print(n.select("a")[0].attrs["href"])
        print(n.text.strip())
        # # print(type(n.text.strip()))
        # print('------------')
        
        link.append(n.select("a")[0].attrs["href"])
        
        '''
        >> STOP <<
         - n.text.strip() 한거 list에 넣기
         - link 들어가서 기사 전문 파싱하기
         
             *** 제목, 날짜, 신문사 => MongoDB
                 기사 전문 => OracleDB
        '''
        # /item/news_read.nhn?article_id=0004619120&office_id=008&code=005930&page=&sm=title_entity_id.basic
        # con = HTTPSConnection("finance.naver.com")
        # for pageIn in :
            # con.request("GET", "/item/news_news.nhn?code=%s&page=%d" % (cCode, page))
            # rb = con.getresponse().read()
            # ssNewsData2 = BeautifulSoup(rb, "html.parser", from_encoding = "utf-8")
            # ssNewsData2 = ssNewsData.select("div#news_read.scr01 span")
            
        

