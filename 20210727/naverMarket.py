# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from http.client import HTTPSConnection

# https://finance.naver.com/item/sise_day.nhn?code=005930&page=2

cCode = '005930'    # 삼성전자

h = {'User-agent' : 'mozilla/5.0'}
d = []

con = HTTPSConnection("finance.naver.com")
for page in range(1, 11):
    con.request("GET", "/item/sise_day.nhn?code=%s&page=%s" % (cCode, page), headers = h)
    rb = con.getresponse().read()
    ssMarketData = BeautifulSoup(rb, "html.parser", from_encoding = "euc-kr")
    ssMarketDatas = ssMarketData.select("td span")
    for m in ssMarketDatas:
        d.append(m.text.strip())

print(d)