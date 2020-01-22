'''
Created on 2020. 1. 22.
@author: GDJ19

    <pandas 모듈을 이용하여 csv 파일을 읽고 써보자>
    - csv파일 : supplier_data.csv
'''

import pandas as pd

input_file = "supplier_data.csv"
output_file = "pandas_out01.csv"

data_frame = pd.read_csv(input_file)
print(type(data_frame))
print(data_frame) # 읽은 csv파일 전체 출력

important_dates = ["1/20/14", "1/30/14"]
data_frame_in_set = data_frame.loc[data_frame["Purchase Date"].isin(important_dates), :]
print(data_frame_in_set)
'''
    loc : 행을 가져오는데,
    data_frame["Purchase Date"] : (컬럼)열의 값 중에서
    isin(important_dates) : important_dates 값을 포함하고 있는
    : : 모든 열(컬럼)
    
    --> 즉, Purchase Date 열의 값 중 "1/20/14", "1/30/14" 값에 속한 모든 컬럼 조회
'''

# 선택된 데이터를 csv 파일로 저장
# to_csv("파일명", index="T/F")
data_frame_in_set.to_csv(output_file, index=False)