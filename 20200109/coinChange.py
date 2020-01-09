'''
Created on 2020. 1. 9.
@author: GDJ19

    <금액을 입력받아 동전으로 바꿔주는 프로그램 작성하기>
    - 500 / 100 / 50 / 10 / 1
    - 동전의 개수를 출력 (동전의 개수는 최소개로 출력할 것)
'''

money = int(input("금액을 입력하세요 : "))

if money >=500 :
    print("500원의 개수 : ", money//500, "개")
money = money%500
print("100원의 개수 : ", money//100, "개")
money = money%100
print("50원의 개수 : ", money//50, "개")
money = money%50
print("10원의 개수 : ", money//10, "개")
money = money%10
print("1원의 개수 : ", money%10, "개")
