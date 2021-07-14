# -*- coding:utf-8 -*-

# 시험 문제 형식

# 2번
# -----
# 1. +
# 2. -
# 3.end
# ===
# what?

# 3이라 쓸때까지 반복

while True:
    print('----')
    print('1. +')
    print('2. -')
    print('3. end')
    m = input('what? : ')
    if m == '3':
        break
    
while True:
    m = input("---\n1...")
    if m == '3':
        break
    elif m == '1':
        x = int(input('x : '))
        y = int(input('y : '))
        print(x+y)
    elif m == '2':
        pass