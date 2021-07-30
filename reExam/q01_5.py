# -*- coding:utf-8 -*-
import numpy as np
from http.client import HTTPConnection
from json import loads
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

con = HTTPConnection("openapi.seoul.go.kr:8088")
con.request("GET", "/4f6a6547456b6368333355736a714f/json/RealtimeCityAir/1/25/")
resBody = con.getresponse().read()
con.close()

airData = loads(resBody)
whereSum = {}
whereCount = {}
guName, sum = None, None

for a in airData["RealtimeCityAir"]["row"]:
    guName = a['MSRRGN_NM']
    sum = float(a['PM10']) + float(a['PM25'])
    if guName in whereSum:
        whereSum[guName] += sum
        whereCount[guName] += 1
        
    else:
        whereSum[guName] = sum
        whereCount[guName] = 1
        
kwonList = []
pmList = []
for k,v in whereSum.items():
    kwonList.append(k)
    pmList.append(v / whereCount[k])
    
kwonList = np.array(kwonList)
pmList = np.array(pmList)

fontFile = "C:\\Users\\sdedu\\Desktop\\test\\malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=20).get_name()
plt.rc("font", family=fontName)

plt.bar(kwonList, pmList)
plt.title("권역별 미세먼지")
plt.xlabel("권역")
plt.ylabel("PM10 + PM25")
plt.show()


