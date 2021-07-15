# -*- coding:utf-8 -*-
# 계속 받아서 새로 쓰는 프로그램
from http.client import HTTPSConnection
from urllib.parse import quote
from bson.json_util import loads
from konlpy.tag._okt import Okt
from wordcloud.wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.utils.tests.test_pprint import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def cut(t):
    return t.replace("<b>", "").replace("</b>", "").replace("&quot;", "").replace("&lt;", "").replace("&gt;", "")

def getData():
    w = quote("휴가")
    
    h = {"X-Naver-Client-Id" : "gHKtdtM_pLs3ZHJb2YCo",
         "X-Naver-Client-Secret" : "qL_1zOFWVU"}
    
    con = HTTPSConnection("openapi.naver.com")
    con.request("GET", "/v1/search/blog.json?query=" + w, headers=h)
    resBody = con.getresponse().read()
    con.close()
    
    vacationData = loads(resBody)
    data = [] # 데이터 확보; 굳이 파일로 저장 안하고 리스트에 담아서 계속 불러와도 됨
    label = []
    what = [None, '정상', '광고']
    for v in vacationData['items']:
        desc = cut(v['description'])    #나중에 써먹을떄 편하게 쓰기위해
        print(desc)
        lb = int(input("1) 정상\n2) 광고\n뭐 : "))
        
        data.append(desc)       # 데이터를 잘 넣었는지 확인
        label.append(what[lb])
        print('-'*15)
    # print(data)
    # print(label)
    return data, label

def showTrend(data):
    o = Okt()
    txt = ''
    for d in data:
        for n in o.nouns(d):
            print(n)
            txt += n + ' '
    print(txt)
    wc = WordCloud(font_path ="C:/Users/sdedu/Desktop/test/malgun.ttf", background_color='white').generate(txt)
    plt.imshow(wc)
    plt.show()
    
def isAd(data, label):
    cv = CountVectorizer()
    cvResult = cv.fit_transform(data).toarray()
    # print(cvResult) # 무슨 단어가 몇번 나왔는지
    mnb = MultinomialNB().fit(cvResult, label)  # 분류기 + 학습시키기
    
    txt = input('글 : ')     # 원래는 크롤링하는거 였는데 너무 커졌다... -> 해보까..?
    vacationCvResult = cv.transform([txt]).toarray()
    result = mnb.predict(vacationCvResult)[0] # 단어수 세서 예측하기
    print(txt, ":", result)
    
    # 5번
    data.append(txt)
    label.append(result)

def showMainMenu():
    print()
    print("------------")
    print("1. 다시 블로그 데이터 받아오기")
    print("2. 블로그 트렌드 확인하기")
    print("3. 광고글 판정하기")
    print("4. 종료하기")
    print("------------")
    return input("뭐 : ")
##########################

data, label = getData()
while True:
    menu = showMainMenu()
    if menu == '1':
        data, label = getData()
    elif menu == '2':
        showTrend(data)
    elif menu == '3':
        isAd(data, label)
    elif menu == '4':
        break
    
