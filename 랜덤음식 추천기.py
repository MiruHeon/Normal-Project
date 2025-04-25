from random import *

food = ["햄버거", "라면", "치킨", "떡볶이", "냉면", "부대찌개", "우삼겹 된장찌개"]

chucheon = input("추천해줘? (Y/N) : ")
if chucheon == "Y":
  print("오늘의 추천음식은 %s 입니다" % choice(food))
else:
  exit = input("끝내고 싶어? (Y/N) : ")
  if exit == "Y":
    break
  else:
    pass
