'''
Created on 2020. 1. 22.
@author: GDJ19
    
    <pandas 예제>
'''

import pandas as pd

df = pd.DataFrame({"A":[1,4,7], "B":[2,5,8], "C":[3,6,9]})

print(type(df))
print(df)

print(df["A"])
'''
    <행 선택하기  (인덱스)>
    - iloc[n] : 순서 기준
    - loc[] : 인덱스 이름 기준
    
    <열 선택하기 (컬럼)>
    - df["컬럼이름"]
'''
print("인덱스 값 조회 : iloc[n], loc[n]")
print(df.iloc[0])
print(df.iloc[1])
print(df.loc[0])
print(df.ix[0]) # 구버전, 실행은되나 오류남

print()
print("iloc와 loc의 차이점에대해 알아보자")
df = pd.DataFrame(data=([[1,2,3],[4,5,6],[7,8,9]]), index=[2,"A",4], columns=[51,52,53])
print(df)
print("df.iloc[2]=> 인덱스 기준 / 순번,순서를 기준으로 출력")
print(df.iloc[2])

print("df.loc[2]=> 인덱스의 이름을 기준으로 출력")
print(df.loc[2])

