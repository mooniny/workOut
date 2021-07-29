# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

#http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/xml/MosquitoStatus/1/10/2020-03-02
f = open("C:\\Users\\sdedu\\Desktop\\test/exam_mosquito.txt", "a", encoding = "utf-8")
con = HTTPConnection("openapi.seoul.go.kr:8088")

for y in range(2020,2022):
    for m in range(1,13):
        for d in range(1,31):
            when = "%d-%02d-%02d" % (y, m, d)
            con.request("GET", "/4f6a6547456b6368333355736a714f/xml/MosquitoStatus/1/5/" + when)
            resBody = con.getresponse().read()
            mqData = fromstring(resBody)
            mqData = mqData.find("row")
            for i in mqData:
                if mqData != None:
                    print(mqData.find("MOSQUITO_DATE"))
                    print(mqData.find("MOSQUITO_VALUE_HOUSE"))
                    print(mqData.find("MOSQUITO_VALUE_PARK"))
                # f.write("%s," % mqData.find("MOSQUITO_DATE"))
                # f.write("%s," % mqData.find("MOSQUITO_VALUE_HOUSE"))
                # f.write("%s," % mqData.find("MOSQUITO_VALUE_PARK"))
                
            # print(mqData)
            
con.close()
f.close()