# -*- coding:utf-8 -*-
from http.client import HTTPConnection, HTTPSConnection
from bs4 import BeautifulSoup

# https://finance.naver.com/item/news_news.nhn?code=005930&page=2
# https://finance.naver.com/item/news.nhn?code=005930
cCode = '005930'

con = HTTPSConnection("finance.naver.com")
for page in range(1, 1194):
    con.request("GET", "/item/news_news.nhn?code=%s&page=%d" % (cCode, page))
    rb = con.getresponse().read()
    # print(rb.decode())
    ssNewsData = BeautifulSoup(rb, "html.parser", from_encoding = "utf-8")
    ssNewsDatas = ssNewsData.select("div.tb_cont table.type5 tbody tr")
    for n in ssNewsDatas:
        # print(n.text)
        print()
        print(n.select("td.title"))[0]
        print(n.select("td.info"))[0]
        print(n.select("td.date"))[0]
        print("-------------------")
        
# con = HTTPConnection("finance.naver.com")
# con.request("GET", "/item/news.nhn?code=005930")
# rb = con.getresponse().read()
# print(rb.decode())