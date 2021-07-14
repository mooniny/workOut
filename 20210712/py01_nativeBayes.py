# -*- coding:utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Native Bayes (전문적이진 않은 베이지안 정리) : 스팸메일, 악플 필터링
#     지도학습
#     예측을 할 때 A일 확률이 B일 확률보다 크면 결론은 A, 안크면 B

data = ['에이 아니잖아여', '쌤이 없는데 어떻게 잘 지내요', '끝이 아니니깐요', '아니오! 평소 같지 않았어요!', '저말은 무시하시죠']

# BoW(Bag of Words) : 단어 수 세기
cv = CountVectorizer()
cvResult = cv.fit_transform(data) # 학습시키고 변환시키고
# print(cv.vocabulary_)   # BoW결과 (단어 인덱스 번호; 갯수 아님)
cvResult = cvResult.toarray()   #변환
# print(cv.get_feature_names())   # 단어들
# print(cvResult) # 문장별로 그 단어의 출현 횟 수

label = ['부정', '뻥', '부정', '승질', '명령']   # 각각 문장이 어떤 문장인지 (지도학습) (ex. '에이 아니잖아여'-> 부정)

mnb = MultinomialNB() # 라이브데이즈 분류기
mnbAI = mnb.fit(cvResult, label)    # 학습

what = ['아니요 쌤 저말은 무시하세요']  # 예측할 문장
whatCvResult = cv.transform(what) # 바꾸고
whatCvResult = whatCvResult.toarray()
print(whatCvResult)

result = mnbAI.predict(whatCvResult)    # 최종 결과
print(result[0])

