# -*- coding:utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

f = open("C:\\Users\\sdedu\\Desktop\\test/naverMovie.txt", "r",encoding = "utf-8")
f2 = open("C:\\Users\\sdedu\\Desktop\\test/naverMovieLabel.txt", "r", encoding = "utf-8")

data = []
for line in f.readlines():
    line = line.replace("\n","").split("|")[6]
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
print(cvResult)

mnb = MultinomialNB().fit(cvResult, label) # 학습시켜서

review = input("리뷰 : ") # 리뷰를 받아서
reviewCvResult = cv.transform([review]).toarray()
result = mnb.predict(reviewCvResult)[0]
print(review, ':', result)



