# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from urllib.parse import quote
from bson.json_util import loads

# def cut(s):
    # s = s.replace("<b>", "").replace("</b>", "").replace("&quot;", "").replace("&lt;", "").replace("&gt;", "")
    # return s
    #
# w = quote("휴가")
#
# h = {"X-Naver-Client-Id" : "gHKtdtM_pLs3ZHJb2YCo",
     # "X-Naver-Client-Secret" : "qL_1zOFWVU"}
     #
# f = open("C:\\Users\\sdedu\\Desktop\\test/naverBlogSearch.txt", "a", encoding = "utf-8")
# f2 = open("C:\\Users\\sdedu\\Desktop\\test/naverBlogSearchLabel.txt", "a", encoding = "utf-8")
#
# con = HTTPSConnection("openapi.naver.com")
# con.request("GET", "/v1/search/blog.json?sort=sim&display=100&query=" + w, headers=h)
# resBody = con.getresponse().read()
# con.close()
# # print(resBody.decode())
#
# blogData = loads(resBody)
# for b in blogData['items']:
    # print(cut(b['description']))
    # print('1) 정상')
    # print('2) 광고')
    # pandan = input('뭐 : ')
    # print('-' * 20)
    # f.write("%s\n" % cut(b['description']))
    # f2.write("%s\n" % pandan)
    #
# f2.close()
# f.close()

##################################################
import matplotlib.pyplot as plt
from wordcloud.wordcloud import WordCloud
from konlpy.tag._okt import Okt

def reBlogData():
    pass
def BlogTrandInfo():
    # wc = {}
    o = Okt()
    f = open("C:\\Users\\sdedu\\Desktop\\test/naverBlogSearch.txt", "r", encoding = "utf-8")
    txt = None
    for txt in f.readlines():
        try:
            txt = o.pos(txt)
        except:
            pass
        # print(txt)
        for w, p in txt:
            if p =='Noun':
                print(w)
                # if w in wc:
                    # wc[w] += w
            else:
                w += w
                
    f.close()
    wc = WordCloud(font_path ="C:/Users/sdedu/Desktop/test/malgun.ttf", background_color='white').generate(w)
    plt.imshow(wc)
    plt.show()


##################################################
      
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing._data import MinMaxScaler
from sklearn.neighbors._classification import KNeighborsClassifier

def adInfo():
    f = open("C:\\Users\\sdedu\\Desktop\\test/naverBlogSearch.txt", "r", encoding = "utf-8")
    f2 = open("C:\\Users\\sdedu\\Desktop\\test/naverBlogSearchLabel.txt", "r", encoding = "utf-8")

    data = []
    for line in f.readlines():
        line = line.replace("\n","").split("...")[0]
        data.append(line)
    
    label = []
    for line in f2.readlines():
        line = line.replace("\n","")
        label.append(line)
    
    f2.close()
    f.close()
########################
    cv = CountVectorizer()
    cvResult = cv.fit_transform(data).toarray()
    # print(cvResult)

    mnb = MultinomialNB().fit(cvResult, label)
    
    mms = MinMaxScaler()
    review = input("글 : ")
    reviewCvResult = cv.transform([review]).toarray()
    result = mnb.predict(reviewCvResult)[0]
    if result == '1':
        print(review, ':', '정상')
    else:
        print(review, ':', '부적합으로 의심됨')
        
    what = [[review, result]]
    what = mms.transform(what)
    
    result = knc.predict(what)[0]
    
    f = open("C:\\Users\\sdedu\\Desktop\\haksup.csv", "a", encoding = 'utf-8')
    f.write('%s, %s\n', (review, result))
    f.close()

def showMenu():
    print("------------")
    print("1. 다시 블로그 데이터 받아오기")
    print("2. 블로그 트렌드 확인하기")
    print("3. 광고글 판정하기")
    print("4. 종료하기")
    print("------------")
    return input("메뉴를 선택하시오 : ")

menu = None
while True:
    menu = showMenu()
    if menu == "1":
        reBlogData()
    elif menu == "4":
        break
    elif menu == "2":
        BlogTrandInfo()
    elif menu == "3":
        adInfo()
    






