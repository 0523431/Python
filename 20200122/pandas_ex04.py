'''
Created on 2020. 1. 22.
@author: GDJ19

    <pandas 모듈을 사용하여 column 조회하기>
'''
import pandas as pd

input_file = "supplier_data.csv"
output_file = "pandas_out03.csv"

data_frame = pd.read_csv(input_file)
# : => 모든 행
# 0번(supplier name)과 3번(cost) 열 조회
df_col = data_frame.iloc[:, [0,3]]
print("==== data_frame.iloc[:, [0,3]] ====")
print(df_col)

# 0:4 => 0행부터 4행까지
# 0:3 => 0열부터 3열까지(supplier name / invoice number / cost)
df_col = data_frame.iloc[0:4, 0:3]
print("==== data_frame.iloc[0:4, 0:3] ====")
print(df_col)

print("==== 모든 행의 invoice number와 cost 컬럼 조회하기  ====")
df_col = data_frame.loc[:, ["Invoice Number", "Cost"]]
print(df_col)

print("==== invoice가 '920-'으로 시작하는 행의 invoice number와 cost 컬럼 조회하기  ====")
df_col = data_frame.loc[data_frame["Invoice Number"].str.startswith("920-"), ["Invoice Number", "Cost"]]
print(df_col)

# 선택된 데이터를 csv 파일로 저장
# to_csv("파일명", index="T/F")
df_col.to_csv(output_file, index=False)
