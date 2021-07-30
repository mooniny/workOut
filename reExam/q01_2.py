# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads
import numpy as np

con = HTTPConnection("openapi.seoul.go.kr:8088")
con.request("GET", "/4f6a6547456b6368333355736a714f/json/RealtimeCityAir/1/25/")
resBody = con.getresponse().read()
con.close()

airData = loads(resBody)
gu = {}
guName, sum = None, None
for a in airData["RealtimeCityAir"]["row"]:
    guName = a['MSRSTE_NM']
    sum = a['PM10'] + a['PM25']
    if guName in gu:
        gu[guName] += sum
    else:
        gu[guName] = sum

guList = []
pmList = []
for k,v in gu.items():
    guList.append(k)
    pmList.append(v)

guList = np.array(guList)
pmList = np.array(pmList)

avgPM = np.mean(pmList)
maxPM = np.max(pmList)
minPM = np.min(pmList)

print("평균 : %.2f" % avgPM)
print("--"*10)
print("제일 깨끗: %.2f" % pmList[pmList == minPM][0])
print(guList[pmList == minPM][0])
print("--"*10)
print("제일 더럽: %.2f" % pmList[pmList == maxPM][0])
print(guList[pmList == maxPM][0])