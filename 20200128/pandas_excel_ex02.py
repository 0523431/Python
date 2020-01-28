'''
Created on 2020. 1. 28.
@author: GDJ19

    <문제>
    - Customer Name 컬럼의 값이 J로 시작하는 행만 선택하여 pandas_output2.xls 파일로 생성하기
'''

import pandas as pd

input_file = "sales_2015.xlsx"
output_file = "pandas_output2.xls"

data_frame = pd.read_excel\
                    (input_file, "january_2015", index_col=None) # 모든 데이터를 읽겠다
                    
data_frame_value = data_frame[data_frame['Customer Name'].str.startswith("J")]

writer = pd.ExcelWriter(output_file)

data_frame_value.to_excel(writer, sheet_name="name_start_J", index=False)

# 이 부분에서 파일로 생성이 됨
writer.save()