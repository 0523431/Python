'''
Created on 2020. 1. 9.
@author: GDJ19

    <삼각형의 높이를 입력받은 후 삼각형 출력하기>
    *
    **
    ***
    ****
'''

length = int(input("삼각형의 높이를 입력하세요 : "))

print("직각삼각형 출력하기")
for i in range(0, length) :
    for j in range(0, i+1) :
        print("*", end="")
    print()

for i in range(1, length+1) :
    print("*" *i)

print("역삼각형 출력하기")
for i in range(length,0,-1) :
    print("*" *i)

print('직각삼각형 출력하기 2')
for i in range(1, length+1) :
    print(" " *(length-i), end="")
    print("*" *i)

print('이등변삼각형 출력하기')
for i in range(1, length+1) :
    print(" " *(length-i), end="")
    print("*" *(i*2-1), end="")
    print(" " *(length-i))
    