# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
import seaborn as sns

'''
    2015년11월 버스노선별 정류장별 시간대별 승하차 인원
http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/xml/CardBusTimeNew/1/5/202011/7730/
'''

fontFile = "C:/Users/sdedu/Desktop/test/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=20).get_name()
plt.rc("font", family=fontName)

busNum = input("버스 번호 : ")
busNum2 = float(busNum)
con = HTTPConnection("openapi.seoul.go.kr:8088")
for y in range (2015, 2022):
    for m in range(1, 13):
        when = '%d%02d' % (y, m)
        for p in range(1,77,5):
            # print('%d/%d/%s/%f' % (p, p+4, when, busNum2))
            con.request("GET", "/4f6a6547456b6368333355736a714f/xml/CardBusTimeNew/%d/%d/%s/%d/" % (p, p+4, when, busNum2))
resBody = con.getresponse().read()
con.close()

busData = fromstring(resBody)
buses = busData.iter("row")
for bn in buses:
    a = bn.iter('SEVEN_ALIGHT_NUM')
    for bb in b:
        print(bb.text)
    break

# weatherData = fromstring(resBody)
# weathers = weatherData.iter('data')
# wfKor = []
# temps = []
# rehs = []
# for w in weathers:
    # wfKor.append(w.find('wfKor').text)
    # temps.append(float(w.find('temp').text))
    # rehs.append(float(w.find('reh').text))
    #
# weatherDF = pd.DataFrame()
# weatherDF['날씨'] = wfKor
# weatherDF['기온'] = temps
# weatherDF['습도'] = rehs
#
# sns.scatterplot(x = '기온', y = '습도', hue = '날씨', data = weatherDF)
# plt.show()