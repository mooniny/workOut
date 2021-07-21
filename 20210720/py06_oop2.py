# -*- coding:utf-8 -*-
from random import randint

# 가위바위보, 누가 끌고 가는 형태x
# but, Python은 동시구현x
# => 가상의 인물 심판을 만들어서 진행시키자

# OOD
class Player:
    
    def fire(self):
        self.hand = int(input("what? : "))

class Friend:
    
    def fire(self):
        self.hand = randint(1, 3)

class Referee:
    ruleBook = [None, 'rock', 'scissors', 'paper']
    
    def readRulebook(self):
        print("-------")
        for i,v in enumerate(self.ruleBook):
            if i != 0:
                print("%d) %s" % (i, v))
        print("-------")
    
    def start(self):    # 게임 진행하기
        p = self.callPlayer()
        f = self.callFriend()
        win = 0
        while True:
            self.readRulebook()
            self.playerFire(p)
            self.friendFire(f)
            self.tellHand(p, f)
            # print(p.hand)
            # print(f.hand)
            t = self.judge(p,f)
            if t == -15963:
                break
            win += t
        self.tellResult(win)
        
    def callPlayer(self):   # 청코너 입장
        return Player()

    def callFriend(self):  # 홍코너 입장
        return Friend
    
    def playerFire(self, p):   # Python은 동시동작x, 먼저 내고
        p.fire()
    
    def friendFire(self, f):   # 너도 내고
        f.fire()
        
    def tellHand(self, p, f):
        print("User : %s" % self.ruleBook[p.hand])
        print("Computer : %s" % self.ruleBook[f.hand])
        
    def judge(self, p, f):        # 판정
        t = p.hand - f.hand
        if t == 0:
            print("DRAW")
            return 0              # 연승세기
        elif t == -1 or t == 2:
            print("USER_LOSS")
            return -15963
        else:
            print("USER_WIN")
            return 1  
        
    def tellResult(self, w):
        print("%d times WIN" % w)
        
#####################

r = Referee()   # 심판이 있고
r.start()


