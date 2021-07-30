from http.client import HTTPConnection
from json import loads
import numpy as np

con = HTTPConnection("openapi.seoul.go.kr:8088")
con.request("GET", "/4f6a6547456b6368333355736a714f/json/RealtimeCityAir/1/25/")
resBody = con.getresponse().read()
con.close()

airData = loads(resBody)
airList = airData["RealtimeCityAir"]["row"]

airSumDict = {}
airCountDict = {}
where, pm = None, None
for a in airList:
    where = a["MSRRGN_NM"]
    pm = float(a['PM10']) + float(a['PM25'])
    
    if where in airSumDict:
        airSumDict[where] += pm
        airCountDict[where] += 1
    else:
        airSumDict[where] = pm
        airCountDict[where] = 1
  
airDict = {}
for k, v in airSumDict.items():
    airDict[k] = v / airCountDict[k] 
# print(airDict)
#################################
kwonList = []
pmList = []
for k, v in airDict.items():
    kwonList.append(k)
    pmList.append(v)
    
kwonList = np.array(kwonList)
pmList = np.array(pmList)
pmMean = np.mean(pmList)
print("평균 : %.1f" % pmMean)
print("-----")
dirtyKwonList = kwonList[pmList > pmMean]
dirtyPmList = pmList[pmList > pmMean]
for i in range(dirtyKwonList.size):
    print("%s : %.1f" % (dirtyKwonList[i], dirtyPmList[i]))
