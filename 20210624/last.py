# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup
# https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108

con = HTTPSConnection("www.weather.go.kr")
con.request("GET","/weather/forecast/mid-term-rss3.jsp?stnId=108")
resBody = con.getresponse().read()
con.close()

weather = BeautifulSoup(resBody, "html.parser", from_encoding = "utf-8")
weathers = weather.select("body.location")
# loc = weathers.find_all("location")
for l in weathers:
    print(l.find("province").text)
    
