'''
Created on 2020. 2. 3.
@author: GDJ19

    <excel파일을 pandas로 읽기>
    - 모든 sheet의 열(column)을 선택해보자
'''

import pandas

inputFile = "sales_2013.xlsx"
outputFile = "pandas_output6.xls"

data_frame = pandas.read_excel(inputFile, sheet_name=None, index_col=None)

column_output = []

# data_frame.items() : sheet 전체
# worksheet_name : sheet 이름
# data : sheet에 해당하는 데이터
for worksheet_name, data in data_frame.items() :
    print(worksheet_name," : worksheet_name 출력")
    column_output.append(data.loc[:, ["Customer Name","Sale Amount"]])

# axis=0 : row를 추가 (이렇게 하면 하나의 컬럼에 붙어서 출력됨)
# axis=1 : column을 추가 (총 컬럼이 6개가 나옴)
select_cols = pandas.concat(column_output, axis=1, ignore_index=True)

writer = pandas.ExcelWriter(outputFile)

select_cols.to_excel(writer, sheet_name="select_column_all", index=False)

writer.save()