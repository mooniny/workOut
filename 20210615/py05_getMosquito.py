# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

f = open("C:\\Users\\llaum\\Desktop\\prActice/mosquito.csv", "a", encoding = "utf-8")
con = HTTPConnection("openapi.seoul.go.kr:8088")

for y in range(2016,2022):
    for m in range(5,11):
        for d in range(1,31):
            when = "%d-%02d-%02d" % (y, m, d)
            con.request("GET", "4f6a6547456b6368333355736a714f/xml/MosquitoStatus/1/5/" + when)
            resBody = con.getresponse().read()
            mqData = fromstring(resBody)
            mqData = mqData.find("row")
            if mqData != None:
                f.write("%s," % when)
                f.write("%s," % mqData.find("MOSQUITO_VALUE_WATER"))
                f.write("%s," % mqData.find("MOSQUITO_VALUE_HOUSE"))
                f.write("%s," % mqData.find("MOSQUITO_VALUE_PARK")
            print(when)
            
con.close()
f.close()

