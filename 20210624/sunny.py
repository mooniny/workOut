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

rain = []
province = []
city = []
wfKor = []
tmx = []
tmn = []

for l in locs:
    weathers = weatherData.iter('data')
    province.append(l.find('province'))
    city.append(l.find('city'))
    for w in weathers:
        rain.append(w.find('rnSt').text)
        wfKor.append(w.find('wf').text)
        tmx.append(float(w.find('tmx').text))
        tmn.append(float(w.find('tmn').text))
    
weatherDF = pd.DataFrame()
weatherDF['강수확률'] = rain
weatherDF['날씨'] = wfKor
weatherDF['도'] = province
weatherDF['시'] = city
weatherDF['최고기온'] = tmx
weatherDF['최저기온'] = tmn
print(weatherDF)



# weatherDF["일교차"] = weatherDF['최고기온'] + weatherDF['최저기온']
# weatherDF = weatherDF.sort_values(by = '일교차', ascending = False)