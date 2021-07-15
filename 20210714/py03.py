'''
컴퓨터와 가위, 바위 , 보 프로그램

질때까지 반복, 연승 횟수

얼마나 이기고 지고 비기는지 카운팅

'''
from random import randint

handList = [None, '가위', '바위', '보']  # 숫자를 문자로 바꾸는 가장 간단한 방법

# def rockSP():
    # print("=="*5)
    # print('1. 가위')
    # print('2. 바위')
    # print('3. 보')
    # print("=="*5)

##########################    
wlC = {}
while True:
    print()
    print("=="*5)
    print('1. 가위')
    print('2. 바위')
    print('3. 보')
    print("=="*5)
    comHand = randint(1, 3)
    userHand = int(input('뭐 낼래? : '))
    t = userHand - comHand
    print('유저 :', handList[userHand])
    print('컴퓨터 :', handList[comHand])
    if t == 0:
        print('무승부')
    elif t == -1 or t == 2:
        print("패배")
        break
    else:
        print('승리')
        
        if w,l in wlC:
            wlC[w] += 1
            wlC[l] += 1
        else:
            wlC[w] = 1
            wlC[l] = 1
                    
    

    

    

# if t == 1:
    # print('가위')
# if t == 2:
    # print('바위')
# if t == 3:
    # print('보')        -> 이방법보다는...list로
    
    
# if userHand == comHand:
    # print("무승부") -> 너무 많이 써야함
    
    

    
