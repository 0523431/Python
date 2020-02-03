'''
Created on 2020. 2. 3.
@author: GDJ19

    <excel파일을 pandas로 읽기>
    - 열을 선택해보자
'''

import pandas as pd

inputFile = "sales_2013.xlsx"
outputFile = "pandas_output4.xls"

# pandas로 데이터를 읽는데, sheet를 지정해줌 = january_2013
data_frame = pd.read_excel(inputFile, "january_2013", index_col=None)

# 모든 내용, 컬럼은 2개만
data_frame_value = data_frame.loc[:,["Customer Name","Purchase Date"]]

writer = pd.ExcelWriter(outputFile)
data_frame_value.to_excel(writer, sheet_name="jan_13_output", index=False)

# 이 부분에서 파일로 생성됨
writer.save()