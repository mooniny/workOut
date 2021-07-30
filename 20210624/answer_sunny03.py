# -*- coding:utf-8 -*-

# [중] Pandas를 활용해, 각 도시별로 강수확률, 최고기온, 최저기온, 일교차의 평균을 구하고, 
# 일교차 기준 내림차순 정렬. 평균 일교차를 출력하고, 
# 평균 일교차보다 일교차가 심한 도시 정보만 콘솔출력. Python소스와 결과를 캡쳐하시오.

import pandas as pd
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

con = HTTPConnection("www.weather.go.kr")
con.request("GET", "/weather/forecast/mid-term-rss3.jsp?stnId=108")
resBody = con.getresponse().read()
con.close()

weatherDF = pd.DataFrame() 
weatherData = fromstring(resBody)
location = weatherData.iter('location') 

for w in location:
    p = w.find("province").text
    c = w.find("city").text
    
    for d in w.iter("data"):
        wf = d.find("wf").text
        tmn = float(d.find("tmn").text)
        tmx = float(d.find("tmx").text)
        rnSt = float(d.find("rnSt").text)
     
        weather_dict = {"도":p, "시":c, "날씨":wf, "최저":tmn ,"최고":tmx, "강수확률":rnSt}
        weatherDF = weatherDF.append(weather_dict, ignore_index = True)


# print(weatherDF)

##############################
weatherDF = weatherDF.groupby("시").mean() #시 기준으로 그룹 정렬
weatherDF["일교차"] = weatherDF['최고'] - weatherDF['최저'] #일교차 생성

weatherDF = weatherDF.sort_values(by='일교차', ascending=True) #일교차 기준 내림차순 정렬

print(weatherDF["일교차"].mean()) #평균 일교차

print("-----------")
print(weatherDF[weatherDF["일교차"] > weatherDF["일교차"].mean()]) #평균 일교차보다 일교차가 심한 도시 정보만 콘솔출력














