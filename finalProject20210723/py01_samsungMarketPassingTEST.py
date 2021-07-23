# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

# https://finance.naver.com/item/sise_day.nhn?code=005930&page=2


con = HTTPSConnection("finance.naver.com")
con.request("GET", "/item/sise_day.nhn?code=005930&page=2" )
rb = con.getresponse().read()
print(rb)
ssMarketData = BeautifulSoup(rb, "html.parser", from_encoding = "euc-kr")
print(ssMarketData)
# ssMarketDatas = ssMarketData.select("iframe html body table.type2 tbody tr td span")
# print(ssMarketDatas)
# for m in ssMarketDatas:
    # print(m.text.strip())