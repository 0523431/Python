'''
Created on 2020. 1. 10.
@author: GDJ19

    <배열 값의 합과 평균을 구하는 함수 작성하기>
'''

# 함수 선언
def getSum(numlist) :
    return sum(numlist) # 합계를 구해주는 함수가 있음
#     sum =0
#     for i in range(0, len(numlist)) :
#         sum += list[i]
#     return sum

def getMean(numlist) :
    # 긴 문장을 두줄로 나눌 때는 \ 역슬레시로 연결
    return sum(numlist) / len(numlist) \
        if len(numlist) > 0 else 0
#     return sum(numlist) / len(numlist) if len(numlist) > 0 else 0
#     return getSum(numlist) / len(numlist)

# main 시작
list1= [2,3,3,4,4,5,5,6,6,8,8]
print("list1의 합 :", getSum(list1))
print("list1의 평균 :", getMean(list1))
print()

list2= []
print("list2의 합 :", getSum(list2))
print("list2의 평균 :", getMean(list2))
print()

print("튜플의 형태()로 넣어줘도 함수값이 나옴 왜? 파라미터 자료형이 정해지지않아서")
tp = (2,3,3,4,4,5,5,6,6,8,8)
print("tp의 합 :", getSum(tp))
print("tp의 평균 :", getMean(tp))
