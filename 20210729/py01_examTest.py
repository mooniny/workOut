# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

#http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/xml/MosquitoStatus/1/10/2020-03-02
f = open("C:\\Users\\sdedu\\Desktop\\test/exam_mosquito.txt", "a", encoding = "utf-8")
con = HTTPConnection("openapi.seoul.go.kr:8088")
con.request("GET", "/4f6a6547456b6368333355736a714f/xml/MosquitoStatus/1/5/" + (when))
resBody = con.getresponse().read()
mqData = fromstring(resBody)
mqData = mqData.find("row")
if mqData != None:
    f.write("%s," % mqData.find("MOSQUITO_DATE"))
    f.write("%s," % mqData.find("MOSQUITO_VALUE_HOUSE"))
    f.write("%s," % mqData.find("MOSQUITO_VALUE_PARK"))
print(mqData)
            
con.close()
f.close()