# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring

# curl "https://openapi.naver.com/v1/search/news.xml?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&sort=sim" \
    # -H "X-Naver-Client-Id: {애플리케이션 등록 시 발급받은 client id 값}" \
    # -H "X-Naver-Client-Secret: {애플리케이션 등록 시 발급받은 client secret 값}" -v
    
def cut(s):
    s = s.replace("<b>", "").replace("</b>", "").replace("&quot;", "")
    return s
   
search = quote(input("검색어 : "))

h = {"X-Naver-Client-Id" : "gHKtdtM_pLs3ZHJb2YCo",
     "X-Naver-Client-Secret" : "qL_1zOFWVU"}

f = open("C:\\Users\\sdedu\\Desktop\\test/naverNews.txt", "a", encoding = "utf-8")

con = HTTPSConnection("openapi.naver.com")
for p in range(1,1001,100):
    con.request("GET","/v1/search/news.xml?query=" + search + "&display=100&start=%d" % (p), headers=h)
    resBody = con.getresponse().read()
    print(resBody.decode())
    con.close()

    newsDate = fromstring(resBody)
    news = newsDate.getiterator("item")
    print(news)
    for i in news:
        print(cut(i.find("title").text))
        # print(cut(i.find("description").text))
        print('---')
        f.write(""(cut(i.find("title").text)))

f.close()







