'''
Created on 2020. 1. 10.
@author: GDJ19

    <dictionary : 예제2>
'''
from operator import __eq__


foods = {"떡볶이":"어묵", "짜장면":"단무지", "라면":"김치", "맥주":"치킨"}

for i in foods.keys() :
    print("%s => %s" % (i, foods[i]))

# 문제
# 화면에서 음식을 입력받아서 궁합음식 출력하기
# "종료"를 입력한 경우 프로그램 종료

cnt =0
while True :
    # foods.keys() : 자료형이 dict_keys
    # 그래서 문자열과 + 연산자로 묶어서 출력할 수 없음
    # left = input(str(foods.keys()) + "중에서 음식을 입력하세요 : ")
    # 근데 자료형을 변환해서 출력하면
    # 출력이 dict_keys(['떡볶이', '짜장면', '라면', '맥주'])
    # 그래서 다시 자료형을 변환시켜줌 ↓
    left = input(str(list(foods.keys())) + "중에서 음식을 입력하세요 : ")
    
    if left == "종료" :
        print("입력 횟수 : ", cnt)
        # print("등록된 음식 개수", foods.count(foods.keys()))
        print("등록된 음식 개수 len(foods) :", len(foods))
        print("등록된 음식 개수 len(foods) : " + str(len(foods)))
        print("왼쪽 음식 :", str(list(foods.keys())))
        print("오른쪽 음식(궁합) :" + str(list(foods.values())))
        
        print()
        print("튜플")
        print(foods.items())
        print(list(foods.items()))
        print(list(foods.items())[-1]) # ('맥주','치킨')

        break
    
    # if와 in의 조합
    # 안에 포함이 되어있는지 안되어있는지를 확인해줌
    if left in foods :
        print("<%s>의 궁합 음식은 <%s>입니다" % (left,foods[left]))
        cnt +=1
    else :
        print("등록된 음식이 아닙니다")
        addLeft = input("추가로 등록하시겠습니까? (Y/N) ")
        if addLeft == "Y" or addLeft == "y" :
            # foods.update({left:input("궁합음식을 입력해주세요")})
            foods[left] = input("궁합음식을 입력해주세요 ")
            print("등록되었습니다")
        else :
            print()
        
#     if left.__eq__(foods.keys()) :
#         print("<%s>의 궁합 음식은 <%s>입니다" % (left,foods[left]))
    
#     if not left.__eq__(foods.keys()) :
#         print("등록되어있지않습니다")
        