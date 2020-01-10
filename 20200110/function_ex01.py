'''
Created on 2020. 1. 10.
@author: GDJ19

    <function : 함수사용하기>
'''

# 함수 선언하기
# 예약어 def로 시작하고 앞에 시작하는 공백으로 구분할 수 있음
def coffee_machine(button):
    print()
    print("#1 뜨거운 물 준비")
    print("#2 개인 머그컵 준비")
    if button ==1 :
        print("#3 보통 커피를 탄다")
    elif button ==2 :
        print("#3 설탕 커피를 탄다")
    elif button ==3 :
        print("#3 블랙 커피를 탄다")
    else :
        print("#3 커피 종류 없음")
    print("#4 물 붓기")

# main 시작
kind = int(input("커피 종류를 입력하세요 (1:보통 / 2:설탕 / 3:블랙) : "))
coffee_machine(kind)