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
weatherData = weatherData.iter('location')
weatherDict = None
city, province = None, None
weatherDF = pd.DataFrame()
for l in weatherData:
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
        
def getSunny(t):
    if t == '맑음':
        return '맑음'
    return '안맑음'

weatherDF['날씨'] = weatherDF['날씨'].apply(getSunny)
weatherDF3 = weatherDF.groupby('날씨').mean()
weatherDF3['일교차'] = weatherDF3['최고'] - weatherDF3['최저']
print(weatherDF3)


sns.barplot(data=weatherDF3, palette='rainbow')
plt.show()






#    맑고 안맑고는 강수 확률에 영향을 주지 않는다.



############################################