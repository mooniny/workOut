# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

cCode = '005930'    #삼성전자

con = HTTPSConnection("finance.naver.com")
link = []
data = []
datas = []
for page in range(1, 5):
    con.request("GET", "/item/news_news.nhn?code=%s&page=%d" % (cCode, page))
    rb = con.getresponse().read()
    # print(rb.decode())        # utf-8
    ssNewsData = BeautifulSoup(rb, "html.parser", from_encoding = "utf-8")
    ssNewsDatas = ssNewsData.select("tbody tr")
    # print(ssNewsDatas)
    for n in ssNewsDatas:
        # print(n.select("a")[0].attrs["href"])   # 링크
        # print(n.text.strip())   # 제목, 신문사, 날짜
        # print(type(n.text.strip())) # str
        # print('------------')
        link.append(n.select("a")[0].attrs["href"])
        data.append(n.text.strip())
        
        con2 = HTTPSConnection("finance.naver.com")         # 기사 전문
        con2.request("GET", n.select("a")[0].attrs["href"])
        rb2 = con2.getresponse().read()
        # print(rb2)        # utf-8
        ssNewsLink = BeautifulSoup(rb2, "html.parser", from_encoding = "utf-8")
        ssNewsLinks = ssNewsLink.select("#news_read")
        # print(ssNewsLinks)
        for l in ssNewsLinks:
            print(l.text.strip())
            print('-------')
            break
            
        
    for txt in data:
        # print(txt)
        # print(type(txt))
        if txt != None and txt != "" and not txt.startswith("관련뉴스") and not txt.startswith('연관기사'):
            txt = txt.replace('/n',' ').split('\n')
            # print(txt)
            # print("-----")
            datas.append(txt)
            
# print(link)
# print(data)
# print(datas)
        
'''
        >> STOP <<
         - n.text.strip() 한거 list에 넣기  => 성공
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
            
        

