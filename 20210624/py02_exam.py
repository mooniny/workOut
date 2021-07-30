# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
import pandas as pd
# https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
con = HTTPConnection("www.weather.go.kr")
con.request("GET","/weather/forecast/mid-term-rss3.jsp?stnId=108")
resBody = con.getresponse().read()
con.close()

weatherData = fromstring(resBody)
weathers = weatherData.iter('body')
weather = weatherData.iter('data')

rain = []
province = []
city = []
wfKor = []
tmn = []
tmx = []
for w in weathers:
    province.append(w.find("province"))
    city.append(w.find("city"))
    
for d in weather:
    rain.append(d.find("rnSt").text)
    wfKor.append(d.find("wf").text)
    tmn.append(float(d.find("tmn").text))
    tmx.append(float(d.find("tmx").text))
        

weatherDF = pd.DataFrame.from_dict({'시':city, 
                                    '도':province,
                                    '강수확률':rain,
                                    '날씨':wfKor,
                                    '최고기온':tmx, 
                                    '최저기온':tmn })
# weatherDF['시'] = city
# weatherDF['도'] = province
# weatherDF['강수확률'] = rain
# weatherDF['날씨'] = wfKor
# weatherDF['최고기온'] = tmx
# weatherDF['최저기온'] = tmn

print(weatherDF)

