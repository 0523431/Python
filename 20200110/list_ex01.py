'''
Created on 2020. 1. 10.
@author: GDJ19

    <list - 리스트 예제>
    - java는 배열과 arrayList가 달랐지만 python은 같아..
    
        (python)
    - list ==> [] == java : Array, list
    - dictionary ==> {} == java : Map
    - tuple ==> () == 상수처리된 list
'''

a = [0, 0, 0, 0] # [] : 리스트, 그러나 거의 배열과 같
b = [] # [] : 리스트, 단 가변배열형태
sumA, sumB =0, 0
for i in range(0,len(a)) : # i = 0,1,2,3
    # list a의 값을 수정
    a[i] = int(input(str(i+1) + "번째 값 : ")) # +연산자는 양쪽 다 문자열인 경우 사용가능
    sumA +=a[i]
    
    b.append(a[i]) #list b에 값을 추가
    print("b의 길이 변화 :", len(b))
    sumB +=b[i]
print(a)
print(b, len(b))
print("리스트 a의 합계 :", sumA)
print("리스트 b의 합계 :", sumB)
