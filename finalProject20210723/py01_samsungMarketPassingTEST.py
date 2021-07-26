# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

# https://finance.naver.com/item/sise_day.nhn?code=005930&page=2
# https://finance.naver.com/item/sise.nhn?code=005930

con = HTTPSConnection("finance.naver.com")
con.request("GET", "/item/sise.nhn?code=005930")
rb = con.getresponse().read()
print(rb)
ssMarketData = BeautifulSoup(rb, "html.parser", from_encoding = "euc-kr")
print(ssMarketData)
# ssMarketDatas = ssMarketData.select("#document")
# print(ssMarketDatas)
# for m in ssMarketDatas:
    # print(m.text.strip())