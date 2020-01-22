'''
Created on 2020. 1. 22.
@author: GDJ19

    <pandas 모듈을 사용하여 csv 파일에 저장하기>
'''

import pandas as pd

input_file = "supplier_data.csv"
output_file = "pandas_out02.csv"

data_frame = pd.read_csv(input_file)
print(type(data_frame))
print(data_frame) # 읽은 csv파일 전체 출력

data_frame_in_set = data_frame.loc[data_frame["Invoice Number"].str.startswith("001-")]
print(data_frame_in_set)
'''
    loc : 행을 가져오는데,
    data_frame["Invoice Number"] : (컬럼)열의 값 중에서
    str.startswith("001-") : 값이 "001-"로 시작
    : : 모든 열(컬럼)
    
    --> 즉, Invoice Number 열의 값 중 "001-"로 시작하는 모든 컬럼 조회
'''

# 선택된 데이터를 csv 파일로 저장
# to_csv("파일명", index="T/F")
data_frame_in_set.to_csv(output_file, index=False)