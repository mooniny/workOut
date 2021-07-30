# -*- coding:utf-8 -*-
import pandas as pd
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fontFile = "C:/Users/sdedu/Desktop/test/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=20).get_name()
plt.rc("font", family=fontName)

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

sns.barplot(x="도", y='강수확률', data=weatherDF, palette='summer')
plt.xticks(rotation = 45)
plt.tick_params(labelsize=7)
plt.title('도 별 강수 확률')
plt.show()









############################################        



############################################      
# 3번
# weatherDF2 = weatherDF.groupby('시').mean()
# weatherDF2['일교차'] = weatherDF2['최고'] - weatherDF2['최저']
# weatherDF2 = weatherDF2.sort_values(by='일교차', ascending=False)
# print(weatherDF2['일교차'].mean())
# print("-------")
# print(weatherDF2[weatherDF2['일교차'] > weatherDF2['일교차'].mean()])    

############################################ 
# 4번
# sns.scatterplot(x='강수확률', y='일교차', data=weatherDF2)
# sns.lmplot(x='강수확률', y='일교차', data=weatherDF2)
# plt.show()
# 강수량과 일교차는 상관없다.
