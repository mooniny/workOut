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
    p = l.find('province').text
    c = l.find('city').text
    for w in l.iter('data'):
        # print(p)
        # print(c)
        # print(w.find('wf').text)        # wfKor.append(w.find('wf').text)
        # print(w.find('tmx').text)       # tmx.append(float(w.find('tmx').text))
        # print(w.find('tmn').text)       # tmn.append(float(w.find('tmn').text))
        # print(w.find('rnSt').text)      # rain.append(w.find('rnSt').text)
        # print("----")
        wf = w.find('wf').text
        tmn = float(w.find('tmn').text)
        tmx = float(w.find('tmx').text)
        rnSt = w.find('rnSt').text
        dict = {"도":p, "시":c, "날씨":wf, '최저':tmn, '최고' :tmx, '강수확률':rnSt}
        weatherDF = weatherDF.append(dict, ignore_index=True)
print(weatherDF)
        
        
    
    
    