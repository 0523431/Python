'''
Created on 2020. 2. 4.
@author: GDJ19

    <numpy>
    - 배열 사본 생성 : copy()
    - 재구조화 : reshape(원하는 편성 구조) / 요소의 개수가 맞아야함 == size:9 재편성 3*3가능, 5*2 불가능
'''

import numpy as np

# 0부터  9까지 임의의 난수 10개를 배열로 저장
x= np.random.randint(10, size=10)
x_sub = x[:2]
print(x)
print(x_sub)

# 사본 x_sub의 0번째 요소를 20으로 바꾸자
# 부분 배열인 x_sub의 요소를 바꾸면 원본 배열 x의 요소도 같이 바뀜을 알 수 있음
x_sub[0] =20
print(x)
print(x_sub)

print("\n배열의 복사")
x_cop = x.copy()
x_cop[0] = 100
print(x)
print(x_cop)

print("\n배열의 재구조(재편성)")
print("1차원 배열인 x를 5행 2열의 2차원 배열로 재편성해보자")
x2 = x.reshape(5,2)
print(x2)

print("0부터 9까지의 임의의 수 9개로 이루어진 배열 생성하고 3행 3열의 배열로 재편성해보자")
y = np.random.randint(10, size=9)
print(y)
y2 = y.reshape(3,3)
print(y2)