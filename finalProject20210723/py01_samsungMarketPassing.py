# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

# https://finance.naver.com/item/sise_day.nhn?code=005930&page=2
cCode = '005930'

con = HTTPSConnection("finance.naver.com")
for page in range(1, 10):
    con.request("GET", "/item/sise_day.nhn?code=%s&page=%d" % (cCode, page))
    rb = con.getresponse().read()
    # print(rb)
    ssMarketData = BeautifulSoup(rb, "html.parser", from_encoding = "euc-kr")
    print(ssMarketData)
    ssMarketDatas = ssMarketData.select("iframe html body table.type2 tbody tr td span")
    # print(ssMarketDatas)
    # for m in ssMarketDatas:
        # print(m.text.strip())


'''
 - 주식시장 일별시세 표, 파싱해서 
    => 날짜, 종가, 전일비, 시가, 고가, 저가, 거래량
    => pandas?
   
 - 기사 수와 전일 대비 등락정도 비교
 
 - 기사 수↑, 상승 => 기사 전문 텍스트 정제시켜서 워드클라우드?!
 - 기사 수↑, 하락 => 
 - 기사 수↓, 상승 => 
 - 기사 수↓, 하락 => 
   
 - 기사 수와 주가의 상관관계 도출 => AI학습으로 매도, 매수 프로그램  
    
'''
    