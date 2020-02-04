'''
Created on 2020. 2. 4.
@author: GDJ19

    <numpy>
'''

import numpy as np

# 0부터 9까지의 숫자로 이루어진 배열
x = np.arange(10)
print("x", x)
print("x[:5]", x[:5])
print("x[5:]", x[5:])
print(x[4:7])
print("0부터 2씩 증가",x[::2])
print("1부터 2씩 증가",x[1::2])
print("1부터 7까지 3씩 증가", x[1:8:3])
print(x[::-1])

print()
print("0부터 9까지의 난수를 4행 5열 2차원 배열에 저장")
x = np.random.randint(10, size = (4,5))
print(x)

print("2개의 행과 3개의 열만 가져와보자")
print(x[:2, :3])

print("모든 행을 가져오고 열은 한개씩 걸러서 가져와보자")
print(x[:, ::2])

print("행과 열을 역순으로 가져와보자")
print(x[::-1, ::-1])

