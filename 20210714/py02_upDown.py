# -*- coding:utf-8 -*-
from random import randint

# up down 게임
#     한명(컴퓨터)이 랜덤한 숫자를 하나 생각
#     다른 사람이 그 숫자를 맞추는 게임

# 컴퓨터가 임의의 숫자를 만들고
# 맞출때까지 반복
# 예상 번호를 입력하고
# 맞으면 정답
# 틀리면 up, down출력 
# 재출력하게 정답유도 

# recursive
def say():
    try:
        n = int(input("guess number : "))
        if 1<=g<=1000:
            return g
        return say()
    except:
        return say()
    
#############################
n = randint(1, 1000)
print(n)

for t in range(1, 1000):
    g = say()
    
    if n > g :
        print("Up~")
    elif n < g:
        print("Down~")
    else:
        print("%d times Correct!" % t)
        break


# 컴퓨터가 랜덤한 숫자를 하나 생각
# n = randint(1, 1000)
# print(n)

# t = 0
# 무한 반복
# while True:
    # 반복 횟 수
    # t += 1
    # 답 제출하기
    # g = int(input("guess number : "))
    
    # if n == g:              => 프로그램 1글자 덜 씀
        # print("Correct!")
        # break
    # elif n > g:
        # print("Up~")
    # elif n < g:
        # print("Down~")      => 확률상 더 많이 걸러내는걸 앞에 배치! (정답률 < 오답률); 검사 횟수 차이가 생김
        
    if n > g :
        print("Up~")
    elif n < g:
        print("Down~")
    else:
        print("%d times Correct!" % t)
        break
    
print("------------------------------")        
        
for t in range(1, 1000):       # 바보가 아닌 이상 1000번 안에는 맞출테니까; 턴 수를 고려하면 이쪽이 더 나음
    g = int(input("guess number : "))
    
    if n > g :
        print("Up~")
    elif n < g:
        print("Down~")
    else:
        print("%d times Correct!" % t)
        break
    