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
# https://finance.naver.com/item/news_read.nhn?article_id=0003942747&office_id=011&code=005930&page=&sm=title_entity_id.basic


con2 = HTTPSConnection("finance.naver.com")         # 기사 전문
con2.request("GET", '/item/news_read.nhn?article_id=0003942747&office_id=011&code=005930&page=&sm=title_entity_id.basic')
rb2 = con2.getresponse().read()
ssNewsLink = BeautifulSoup(rb2, "html.parser", from_encoding = "utf-8")
ssNewsLinks = ssNewsLink.select("div#news_read .scr01")   # article3.xml
print(ssNewsLinks)

        # for l in ssNewsLinks:
            # if l in n.select(".info"):
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


