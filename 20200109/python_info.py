'''
Created on 2020. 1. 9.
@author: GDJ19

특징 (자바와 비교했을 때)
1. 변수 선언이 필요없음
2. {} 블럭이 필요없음
    - if, 반복문 내부에서 블록표시가 없음
    - 표현 방법 : 공백으로 (줄맞춤)
3. 주석 표현 방법
    - 여러줄 : ''' '''
    - 한줄 : #
'''

sel = int(input('입력 진수 결정(16/10/8/2) : '))
'''
    input : String
    int(input()) => 형변환 
    
    num = input() : 문자열
'''
num = input("값 입력 : ")
if sel ==16 :
    num10 = int(num,16)
    print("16진수 "+num+", 10진수로 바꾼 값")
if sel ==10 :
    num10 = int(num,10)
if sel ==8 :
    num10 = int(num,8)
if sel ==2 :
    num10 = int(num,2)
print(num10)

print(type(num)) # input으로 받았으니까 문자열
num = num10
print(type(num)) # 자료형이 동적으로 변함

# 10진수를 진법으로 출력해보자
print("16진수 => ", hex(num10))
print("8진수 => ", oct(num10))
print("2진수 => ", bin(num10))
