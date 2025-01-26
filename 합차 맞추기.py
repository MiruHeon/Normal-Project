from random import *
import time
import os
life = 5
score = 0

level = input("난이도 설정! 쉬움 / 노멀 / 하드 : ")

while True:
    op = randint(0,1)
    if life == 0:
        print("<Game Over>")
        print('<최고점수: %d점>' % score)
        break
    else:
        print("남은 목숨 :", life ,"개 현재 스코어 :", score,'점')
        if level == "쉬움":
            A = randint(1,9)
            B = randint(1,9)
        elif level == "노멀":
            A = randint(10,99)
            B = randint(10,99)
        elif level == "하드":
            A = randint(100,999)
            B = randint(100,999)
        if op == 0:
            C = A+B
            print(A,"+",B,"=", end=" ")
            user = int(input(""))
            print(A,"+",B,"=",C)
            if C == user:
                print("맞았습니다.")
                score += 100
            else:
                print("틀렸습니다.")
