# -*- coding:utf-8 -*-
from random import randint

# 입력 / 랜덤 : 숫자, 결과출력 : 글자처리 편하게 하려고
handList = [None, '가위', '바위', '보']

# 반복문 속에서 계속 필요한 기능이니 -> 정리차원에서... 
def showRule():
    print("=="*5)
    for i,v in enumerate(handList):
        if i != 0:
            print("%d) %s" % (i, v))
    print("=="*5)
    
# 반복문 속에서 계속 필요한 기능이니 -> 정리차원에서...
# 잘못 입력한거 다시 -> recursive
def userFire():
    try:
        uh = int(input("뭐 : "))
        if 1 <= uh <= 3:
            return uh
        print("1, 2, 3 중에 써주시기 바랍니다.")
    except:
        print("숫자로 입력 바랍니다.")
        return userFire()

# 유저가 손 내는 것과 통일성...
def comFire():
    return randint(1, 3)

# 반복문 속에서 계속 필요한 기능이니 -> 정리차원에서...
def printHand(uh, ch):
    print("유저 : %s" % handList[uh])
    print("컴터 : %s" % handList[ch])

# 반복문 속에서 계속 필요한 기능이니 -> 정리차원에서...    
def judge(uh, ch):
    t = uh - ch
    
    if t == 0:
        print("무승부")
        return 0
        # return False
    elif t == -1 or t == 2:
        print("패배")
        return -4897
        # return True
    else:
        print("승리")
        return 1
        # return False
        
def printScore(w):
    print("%d연승" % w)
        
########################## 
userHand, comHand, t, win = None, None, None, 0
while True:
    showRule()
    userHand = userFire()
    comHand = comFire()
    printHand(userHand, comHand)
    t = judge(userHand, comHand)
    if t == -4897:
        break
    win += t
printScore(win)

    

    
