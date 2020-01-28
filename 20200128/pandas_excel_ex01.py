'''
Created on 2020. 1. 28.
@author: GDJ19

    <excel파일을 pandas로 읽기>
    - pandas는 엑셀파일을 표로 읽어냄
    - sheet가 있는 경우 역시, 선택해서 읽을 수 있음
'''

import pandas as pd

input_file = "sales_2015.xlsx"
output_file = "pandas_output.xls"

data_frame = pd.read_excel\
                    (input_file, "january_2015", index_col=None) # 모든 데이터를 읽겠다

# data_frame_value : 조건에 맞는 데이터만 저장하고 있는 변수
# 즉, 컬럼의 이름이 Sale Amount인 컬럼을 가져오는데, float타입으로 300.0보다 큰 아이들만 가져와라
data_frame_value = data_frame[data_frame['Sale Amount'].astype(float) > 500.0]

# 데이터가 저장될 빈 excel파일을 만들어줌
writer = pd.ExcelWriter(output_file)

# 조건에 맞는 데이터를 저장하는데 excel파일로 바꿔서 저장 to_excel
data_frame_value.to_excel(writer, sheet_name="jan_15_output", index=False)

# 이 부분에서 파일로 생성이 됨
writer.save()