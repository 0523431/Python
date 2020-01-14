'''
Created on 2020. 1. 14.
@author: GDJ19

    <Lambda식을 이용한 리스트 처리>
'''

myList = [1,2,3,4,5]

def add10(num) :
    return num +10

# main
for i in range(len(myList)) :
    myList[i] =add10(myList[i])
print(myList) # [11, 12, 13, 14, 15]

# lambda
add = lambda num : num+10
for i in range(len(myList)) :
    myList[i] =add(myList[i])
print(myList) # [21, 22, 23, 24, 25]

# lambda 즉시 처리
for i in range(len(myList)) :
    myList[i] =(lambda num : num+10)(myList[i])
print("람다 즉시처리",myList) # [31, 32, 33, 34, 35]
