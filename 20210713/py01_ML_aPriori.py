# -*- coding:utf-8 -*-
from apyori import apriori

# scikit-learn에 없음
# pip install apyori

# a priori - 추천 시스템 (인공지능 < 확률)
#     비지도학습
#     데이터의 연관 분석

# 지지도
#     총 400명이 장을 봤는데 그중 한명만 막걸리를 샀다. => 막걸리로 추천 시스템을 쓰기엔 샘플이 너무 적음.

# 신뢰도
#     치킨을 구매한 사람이 맥주를 구매할 확률은?
#     치킨 구매 -> 맥주를 구매할 확률 (1/2 확률)
#     맥주 구매 -> 치킨을 구매할 확률 (1/3 확률)
# a : 맥주, 치킨
# b : 맥주
# c : 맥주
# d : 치킨

data = [['beer', 'chicken'],['beer','beer','pizza'],['beer', 'pizza'],['soju'], ['pizza','makgirli','soju']]

result = apriori(data, min_support = 0.4, min_confidence = 0.3)   # 5명중에 40프로 넘는 것만(지지도) 대상으로 (신뢰도) 0.3이상만
result = list(result)
for r in result:
    # print(r)
    # print(r.ordered_statistics)
    for r2 in r.ordered_statistics:
        print(r2)
        print(r2.items_base, '를 산 사람이')
        print(r2.items_add, '를 살 확률이')
        
        print(list(r2.items_base), '를 산 사람이')
        print(list(r2.items_add), '를 살 확률이')
        print(r2.confidence)
        print(r2.lift)
        print('------')
        
# lift = p(치킨, 맥주) / (p(치킨) * p(맥주))
        # 같이 나올 확률 / 각각 따로 나올 확률
        # 독립일때 보다 같이 얼마나 더 잘 나오나     
        
# list, set, dict중에 set - 중복제거, 순서 렌덤       
# frozenset : set인데 수정불가
