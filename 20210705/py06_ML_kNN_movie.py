# -*- coding:utf-8 -*-

# scikit-learn : python machinelearning library

# pip install sklearn
# pip install numpy==1.16.4        -> 최신버전 오류가 많아서 다운그레이드

# AI
#    MachineLearning : 어떤 문제를 해결하는데 필요한 알고리즘을 사람이 지정해주면
#        여태 해왔던 것들을
#        좀 더 AI스러운 알고리즘을 몇 개 봅시다.
#    DeepLearning : 어떤 문제를 해결하는데 필요한 알고리즘도 직접 찾아서 문제 해결
#        tensorflow로 인공신경망...

#    지도학습
#           영화A - 액션 
#           영화B - 조폭
#            ...     기존 사람들이 판정해놓은 거를 알려주고, 미지의 데이터를 예측
#    비지도학습
#           영화A
#           영화B
#            ...     그 학습데이터의 특징을 찾는 (비슷 한 거 끼리 묶기, ...)

# kNN (k-Nearest Neighbor) 알고리즘 : 학습데이터랑 비슷한걸로 최종 결론 내주는
#    사람을 많이 봐 왔음, 사람 비슷한 거를 보고 사람이라 판정함
#    지도학습
#    데이터를 그래프 상의 점으로 표현
#    예측해야하는 데이터도 점으로 표현
#    예측데이터와 가장 가까운 학습데이터를 k개 찾아서 (점 사이의 거리 - 피타고라스의 정리)
#    다수결로 최종 결론 내는
import numpy as np
from sklearn.neighbors._classification import KNeighborsClassifier

data = np.array([[80,20],[95,5],[10,90],[90,10],[5,95]])
label = np.array(['Action', 'Action', 'Noire', 'Noire', 'Action'])

knc = KNeighborsClassifier(3)   # 가장 가까운 3개 뽑아서 결론...
knc.fit(data, label)    # 학습시키기

x = float(input("Fight Scene : "))
y = float(input("Bad Language : "))
what = np.array([[x,y]])
result = knc.predict(what)      # 결론 내기
print(result[0])    # 예쁘게 글자만 나오게














