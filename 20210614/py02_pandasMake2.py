# -*- coding:utf-8 -*-
import pandas as pd
from http.client import HTTPSConnection
from urllib.parse import quote
from json import loads
# https://openapi.naver.com/v1/search/book.json
title = quote(input("제목 : "))

h = {"X-Naver-Client-Id": "gHKtdtM_pLs3ZHJb2YCo",
     "X-Naver-Client-Secret": "qL_1zOFWVU"}

con = HTTPSConnection("openapi.naver.com")
con.request("GET", "/v1/search/book.json?query=%s" % title, headers=h)
resBody = con.getresponse().read()
print(resBody.decode())
con.close()

books = loads(resBody)
books2 = books["items"]

bookDF = pd.DataFrame(books2)
print(bookDF)
# print(bookDF.iloc[2])
# print(bookDF["price"])










