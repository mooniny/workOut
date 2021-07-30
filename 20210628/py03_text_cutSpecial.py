# -*- coding:utf-8 -*-
from sys import maxunicode
from unicodedata import category

data = ["아이고!!!", "네~", "***아임헝그리***"]

# unicode : 문자 표현 방식
# unicode transformation format - 8bit
#print(maxunicode)   # 유니코드 총 갯수
#print(chr(1210))    # 유니코드 번호 -> 해당하는 번호의 문자
# for i in range(maxunicode):
    # print(chr(i)) # 유니코드 데이터 전체보기
    # print(category(chr(i)))     # 유니코드 카테고리
    # if category(chr(i)).startswith("p"):        # P로 시작하는 카테고리 보기    
        # print(chr(i))

data = ["아이고!!!", "네~", "***아임헝그리***"]
for d in data:
    for i in range(maxunicode):
        if category(chr(i)).startswith("P"):
            d = d.replace(chr(i), " ")
    print(d)
    
    
# 다혜쓰

# unicode : 문자 표현 방식
# utf-8 : unicode transformation format - 8bit

# https://www.compart.com/en/unicode/


print(maxunicode)       # 유니코드의 총 개수
print(chr(1210))        # 1210번째 유니코드 캐릭터 출력
print("--------------------------")

for i in range(maxunicode):
    print(category(chr(i)))
    print("--------------------------")
    
    if category(chr(i)).startswith("P"):        # P for Punctuation
        print(chr(i))   # 해당하는 모든 문자 출력
