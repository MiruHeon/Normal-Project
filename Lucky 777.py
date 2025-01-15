from random import *

print("★" * 15)
print("Lucky 777")
print("★" * 15)
money = 0

gc = int(input("게임을 선택하세요. 1.Go and Stop : "))

if gc == 1:
    while True:
        print("★현재 돈 : %d원★" % money)
        random1 = randint(1,10)
        random = randint(1,10)
        print("<랜덤으로 숫자가 배부 되었습니다.>")
        print("사장님의 숫자는 %d 입니다.\n" % random)
        dop = input("포기하시겠습니까? 네/아니요 : ")
        if dop == '네':
            print("포기합니다.\n")
            print("내 숫자 : %d 상대 숫자 : %d\n" % (random,random1))
        if dop == '아니요':
            if random < random1:
                print("내 숫자 : %d 상대 숫자 : %d" % (random,random1))
                print("<게임에서 패배하셨습니다>")
                money = money - 100
                re = input("계속하시겠습니까? 네/아니요 : ")
                if re == '네':
                    print("게임을 계속합니다.\n")
                elif re == '아니요':
                    print("게임을 그만합니다.\n")
                    break
                else:
                    print("잘못된 입력입니다.\n")
            elif random == random1:
                print("내 숫자 : %d 상대 숫자 : %d" % (random,random1))
                print("<무승부 입니다>")
                re = input("계속하시겠습니까? 네/아니요 : ")
                if re == '네':
                    print("게임을 계속합니다.\n")
                elif re == '아니요':
                    print("게임을 그만합니다.\n")
                    break
                else:
                    print("잘못된 입력입니다.\n")
            else:
                print("내 숫자 : %d 상대 숫자 : %d" % (random,random1))
                print("<게임에서 승리하셨습니다>")
                money = money + 100
                re = input("계속하시겠습니까? 네/아니요 : ")
                if re == '네':
                    print("게임을 계속합니다.\n")
                elif re == '아니요':
                    print("게임을 그만합니다.\n")
                    break
                else:
                    print("잘못된 입력입니다.\n")
else:
    print("잘못된 입력입니다.")
            
