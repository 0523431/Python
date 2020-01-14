'''
Created on 2020. 1. 14.
@author: GDJ19

    <try_catch : 예외처리>
'''

mystr = "파이썬 공부 중입니다. 열심히 파이썬을 공부합시다."
strpython = [] # 파이썬 문자의 위치를 저장할 list
index =0
while True :
    try :
        # index("", index)
        #       --  -----
        #     찾는 값      index이후 값
        str = "공부"
        index = mystr.index(str, index)
        strpython.append(index)
        index +=1
    except :
        break

print(str, "문자 위치 :", strpython, "문자 개수 :",len(strpython))