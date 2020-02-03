'''
Created on 2020. 2. 3.
@author: GDJ19

    <excel파일을 pandas로 읽기>
    - 모든 sheet 조회하는데 row에 조건을 줘서 선택할 수 있음
'''

import pandas as pd

inputFile = "sales_2013.xlsx"
outputFile = "pandas_output5.xls"

# sheet_name=None : 모든 sheet
# 즉, data_frame은 모든 sheet를 저장하고 있음
data_frame = pd.read_excel(inputFile, sheet_name=None, index_col=None)

# list형태
row_output = []

# items()를 붙임으로써 모든 sheet 가져오는거고
# data_frame.items() : 모든 sheet를 선택
# data : sheet에 대행하는 데이터 내용 저장
for worksheet_name, data in data_frame.items() :
    print("=====", worksheet_name, "=====")
    
    # 리스트에 하나씩 추가 append()하는데
    # 조건이 있어
    # Sale Amount가 2000보다 큰 값 (그 과정에서 $와 ,를 다 ''으로 대체해서 순수한 숫자로 만들어줌)
    row_output.append(data[data['Sale Amount'].replace('$','').replace(',','').astype(float) > 2000.0])

# axis=0 : row로 추가
# axis=1 : column으로 추가 (이렇게 설정하면, column위치가 sheet별로 다르게 출력됨)
filtered_row = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(outputFile)
filtered_row.to_excel(writer, sheet_name="sale_amount_gt2000", index=False)

writer.save()
