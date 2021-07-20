# -*- coding:utf-8 -*-

# 가위바위보, 누가 끌고 가는 형태x
# but, Python은 동시구현x
# => 가상의 인물 심판을 만들어서 진행시키자

# OOD
class Player:
    pass

class Friend:
    pass

class Referee:
    def start(self):    # 게임 진행하기
        pass
    
    def callPlayer(self):   # 청코너 입장
        pass

    def callFriend(self):  # 홍코너 입장
        pass
    
    def playerFire(self):   # Python은 동시동작x, 먼저 내고
        pass
    
    def friendFire(self):   # 너도 내고
        pass
    
    def judge(self):        # 판정
        pass
    
#####################

r = Referee()   # 심판이 있고
r.start()


