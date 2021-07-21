# -*- coding:utf-8 -*-
from random import randint


class Player:

    def fire(self):
        self.hand = int(input("뭐 : "))

class Friend:

    def fire(self):
        self.hand = randint(1, 3)

class Referee:
    ruleBook = [None, "가위", '바위', '보']
    
    def readRulebook(self):
        print("-----")
        for i, v in enumerate(self.ruleBook):
            if i != 0:
                print("%d) %s" % (i, v))
        print("-----")

    def callPlayer(self):
        return Player()
    
    def callFriend(self):
        return Friend()

    def playerFire(self, p):
        p.fire()
    
    def friendFire(self, f):
        f.fire()
        
    def tellHand(self, p, f):
        print("유저 : %s" % self.ruleBook[p.hand])
        print("컴터 : %s" % self.ruleBook[f.hand])

    def start(self):
        p = self.callPlayer()
        f = self.callFriend()
        win = 0
        while True:
            self.readRulebook()
            self.playerFire(p)
            self.friendFire(f)
            self.tellHand(p, f)
            t = self.judge(p, f)
            if t == -234:
                break
            win += t
        self.tellResult(win)
        
    def tellResult(self, w):
        print("%d연승" % w)
       
    def judge(self, p, f):
        t = p.hand - f.hand
        if t == 0:
            print("무승부")
            return 0
        elif t == -1 or t == 2:
            print("유저 패")
            return -234
        else:
            print("유저 승")
            return 1

###################
r = Referee()
r.start()