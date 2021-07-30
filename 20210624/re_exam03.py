# -*- coding:utf-8 -*-
import pandas as pd
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

con = HTTPConnection("www.weather.go.kr")
con.request("GET", "/weather/forecast/mid-term-rss3.jsp?stnId=108")
resBody = con.getresponse().read()
con.close()

weatherData = fromstring(resBody)
locs = weatherData.iter('location')
weatherDict = None
city, province = None, None
weatherDF = pd.DataFrame()
for l in locs:
    weatherDict = {}
    province = l.find('province').text
    city = l.find('city').text
    for w in l.iter('data'):
        weatherDict["도"] = province
        weatherDict["시"] = city
        weatherDict["날씨"] = w.find('wf').text
        weatherDict['최저'] = float(w.find('tmn').text)
        weatherDict['최고'] = float(w.find('tmx').text)
        weatherDict['강수확률'] = float(w.find('rnSt').text)
        weatherDF = weatherDF.append(weatherDict, ignore_index=True)
# print(weatherDF)

weatherDF2 = weatherDF.groupby('시').mean()
weatherDF2['일교차'] = weatherDF2['최고'] - weatherDF2['최저']
weatherDF2 = weatherDF2.sort_values(by='일교차', ascending=False)
print("평균 일교차 : ",weatherDF2['일교차'].mean())
print("-------")
print(weatherDF2[weatherDF2['일교차'] > weatherDF2['일교차'].mean()]) 

