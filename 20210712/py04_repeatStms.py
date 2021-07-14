# -*- coding:utf-8 -*-
from random import randint

# 반복문
# 컬렉션 탐색 : for
l = [1, 23, 12, 3]
for asd in l:       # asd = v -> valve(값)
    print(asd)
print("------")
    
l2 = [[10,123], [234, 11], [23, 11]]    # 2차원
for lst in l2:
    # print(lst)
    for v in lst:
        print(v)
print("------")    

# 0 ~ 4까지
l3 = [0,1,2,3,4]
for v1 in l3:
    print(v1)
    
# r = range(5)
# r = list(r)
# print(r)

l3 = list(range(5))
for v2 in l3:
    print(v2)
    
for v3 in list(range(5)):
    print(v3)    
    
for v4 in range(5):
    print(v4)   
print("---------------")

# 00 01 02 10 11 12 20 21 22

for i in range(3):
    # print(i)
    for j in range(3):
        print("%d%d" % (i, j))
print("---------------")    

# 000 001 010 011 020 021 030 031 100 101 110 111 120 121 130 131
for i in range(2):
    for j in range(4): 
        for k in range(2):
            print('%d%d%d' % (i, j, k))
print("---------------") 

for i in range(5):
    for j in range(i+1):
        print('ㅋ', end='')
    print()  
     
print()           
print(">>>>>>>>>>>>>>>>>")            
print()  

# 반복조건 : while
x = randint(1, 5)
print(x)
while x != 5: # 조건 : 5나올때까지, 5나오묜 멈춤
    x = randint(1, 5)
    print(x)
    
x = None    # 변수를 만들기만하고, 어차피 아랫쪽에 썼는데 뭐하러 두번씀
while x != 5:
    x = randint(1, 5)
    print(x)
    
x = None    
while True:     # 최소 한번은 돌게 됐으니까
    x = randint(1, 5)
    print(x)
    
    if x == 5:
        break
print("---------------")

for i in range(5):
    if i == 3:
        # break  # 조건이 되는 순간 반복문 중단, 끝
        continue # 조건이 되는 순간 강제 반복
    print(i)
print("---------------")

# 00만 출력하고 싶음
for i in range(3):
    for j in range(3):
        if j == 1:
            break       # 파이썬 제어 못함 
        print(i, j)
        
# 해결책
go = True
for i in range(3):
    for j in range(3):
        if j == 1:
            go = False
            break
        print(i, j)
    if go == False:
        break





