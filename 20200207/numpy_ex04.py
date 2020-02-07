'''
Created on 2020. 2. 7.
@author: GDJ19
    
    <numpy>
    - 배열의 연결 : concatenate() / vstack / hstack
    - 배열의 분할 : 
'''
import numpy as np

# 같은 차원의 배열 연결
x = np.array([[1,2,3], [4,5,6]])
y = np.array([[3,2,1], [6,5,4]])
print(x)
print(y)
print(np.concatenate([x,y], axis=0)) # 수직연결
print(np.concatenate([x,y], axis=1)) # 수평연결

# 혼합된 차원의 배열 연결
x = np.array([[1,2,3], [4,5,6]]) # 2행 3열
y = np.array([[3,2,1], [6,5,4], [3,2,1]]) # 3행 3열
z = np.array(([7],[10])) # 2행 1열

print(z)
print(np.vstack([x,y])) # x와 y의 수직 스택 (열 column의 길이가 갈아야함)
print(np.hstack([x,z])) # x와 y의 수평 스택 (행 길이가 같아야함)
'''
    np.vstack([x,z]) => 오류 : 열 길이가 다름
    np.hstack([y,z]) => 오류 : 행 길이가 다름
'''

# 배열의 분리
x = np.arange(16).reshape((4,4)) # 0부터 15까지의 값을 가진 배열을 4행 4열 배열로 다시 만듦
print("\narray x\n",x)
upper, lower = np.vsplit(x, [2]) # 2행을 기준으로 자름
print(upper)
print(lower)
left, right = np.hsplit(x, [2]) # 2열을 기준으로 자름
print(left)
print(right)
