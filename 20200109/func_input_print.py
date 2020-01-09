'''
Created on 2020. 1. 9.
@author: GDJ19

<function>
    input("입력전 출력 문자열") : 기본적으로 문자열을 입력 받음
    print(출력값1, 출력값2, ...) : 여러개 출력시 ,쉼표로 연결 가능
    
'''

a = int(input("값1 입력 : "))
b = int(input('값2 입력 : '))
result = a+b
print(a, "+", b, "=", result) # java의 println과 비슷

# 오류 발생 int와 str 사이
# print(a + "+" + b + "=" + result)

print("%d+%d=%d" % (a, b, result)) # java의 printf와 비슷

print("안녕하세요 ", end="") # java의 print와 비슷(한줄 출력)
print("크림블입니다")

# format 함수를 이용하기
print("format 함수 이용하기")
print("{0:d} {1:5d} {2:05d}".format(100,200,300))
'''
    0번째 숫자를 출력 : 100
    1번째 숫자를 출력하는데 5자리를 확보하고 출력 : __200
    2번째 숫자를 출력하는데 5자리 확보하고 빈자리는 0으로 채워서 출력 : 00300
'''
print("{2:d} {1:5d} {0:05d}".format(100,200,300))
'''
    2번째 숫자를 출력 : 300
    1번째 숫자를 출력하는데 5자리 확보하고 출력 : __200
    0번째 숫자를 출력하는데 5자리 확보 빈자리는 1로 채워서 출력 : 00100
'''