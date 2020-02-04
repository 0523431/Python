'''
Created on 2020. 2. 4.
@author: GDJ19

    <numpy>
    - python에서 사용되는 리스트 형태의 수치 처리 모듈
'''

import numpy

# 수치 리스트 생성하기
print(numpy.array([1, 4, 2, 5, 3]))
print(numpy.array([3.14, 4, 2, 3]))
print(numpy.array([1, 2, 3, 4], dtype="float32"))
print()

# 기본 함수
print("10개의 요소를 0으로 채워")
arr = numpy.zeros(10, dtype=int)
print(arr,"\n")

print("3행 5열 리스트를 생성하는데, 1로 채워 (ones) 그리고 이건 2차원 배열")
arr = numpy.ones((3,5), dtype=float)
print(arr,"\n")

print("3행 5열 리스트를 생성하는데, 3.14로 채워 그리고 이건 2차원 배열")
arr = numpy.full((3,5), 3.14)
print(arr,"\n")
print()

print("0에서 시작해서 2씩 더해 20까지 채우는 리스트 생성")
arr = numpy.arange(0, 20, 2)
print(arr,"\n")

print("0과 1 사이를 일정한 간격으로 5번 나눠, 다섯개의 값으로 채운 리스트 생성")
arr = numpy.linspace(0, 1, 5)
print(arr,"\n")

print("3*3 크기의 난수 리스트 생성")
arr = numpy.random.random((3,3))
print(arr,"\n")

print("평균 0, 표준 편차 1의 정규 분포를 따르는 3*3 난수 리스트 생성")
arr = numpy.random.normal(0, 1, (3,3))
print(arr,"\n")

print("0과 9를 포함한 구간의 임의의 정수로 채운 3*3 리스트 생성")
arr = numpy.random.randint(0, 10, (3,3))
print(arr,"\n")

print("ndim : 배열(리스트)의 n차원을 리턴")
print(arr.ndim) # 2

print("shape : 각 n차원의 크기 리턴")
print(arr.shape) # (3, 3)

print("size : 전체 배열의 크기 리턴, 전체 요소의 개수")
print(arr.size) # 9

print("dtype : 배열 요소의 자료형")
print(arr.dtype) # int32




