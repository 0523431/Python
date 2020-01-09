'''
Created on 2020. 1. 9.
@author: GDJ19

    <숫자를 입력받아, 입력수까지의 합>
'''

num = int(input("숫자를 입력하세요 : "))
sum =0
for i in range(1, num+1) :
    sum +=i
print("1부터 ",num,"까지의 합 :",sum)

j =0
sum =0
while j <=num :
    sum +=j
    j +=1
print("1부터 ",num,"까지의 while을 이용한 합 :",sum)

sum =0
for i in range(0, num+1, 2) :
    sum +=i
print("1부터 ",num,"까지 짝수의 합 :",sum)

sum =0
for i in range(1, num+1, 2) :
    sum +=i
print("1부터 ",num,"까지 홀수의 합 :",sum)
