from random import *
import time
import os
life = 5
score = 0

level = input("난이도 설정! 쉬움 / 노멀 / 하드 : ")

while True:
    s200 = randint(1,5)
    l2 = randint(1,4)
    op = randint(0,1)
    if life == 0:
        print("<Game Over>")
        print('<최고점수: %d점>' % score)
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
            if s200 == 1:
                print("200점 짜리 문제입니다.")
            else:
                pass
            if l2 == 2:
                print("life 2개짜리 문제입니다.")
            else:
                pass
            C = A+B
            print(A,"+",B,"=", end=" ")
            user = int(input(""))
            print(A,"+",B,"=",C)
            if C == user:
                print("맞았습니다.")
                if s200 == 1:
                    score += 200
                else:
                    score += 100
                if l2 == 2:
                    life += 2
                else:
                    pass
            else:
                print("틀렸습니다.")
                life -= 1
        else:
            if s200 == 1:
                print("200점 짜리 문제입니다.")
            else:
                pass
            if l2 == 2:
                print("life 2개짜리 문제입니다.")
            else:
                pass
            C = A-B
            print(A,"-",B,"=", end=" ")
            user = int(input(""))
            print(A,"-",B,"=",C)
            if C == user:
                print("맞았습니다.")
                if s200 == 1:
                    score += 200
                else:
                    score += 100
                if l2 == 2:
                    life += 2
                else:
                    pass
            else:
                print("틀렸습니다.")
                life -= 1
    time.sleep(1)
    os.system("cls")
