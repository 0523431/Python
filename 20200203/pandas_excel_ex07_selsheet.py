'''
Created on 2020. 2. 3.
@author: GDJ19

    <excel파일을 pandas로 일기>
    - pandas는 표
    - sheet를 선택해서 조회해 보자
'''

import pandas

inputFile = "sales_2013.xlsx"
outputFile = "pandas_output7.xls"

# 첫번째, 두번째 sheet만 선택
my_sheets = [0, 1]
threshold = 1900.0

data_frame = pandas.read_excel(inputFile, sheet_name=my_sheets, index_col=None)

row_list = []

#선택된 sheet의 내용 중 Sale Amount의 값이 1900보다 큰 값을 가진 행을 선택
for worksheet_name, data in data_frame.items() :
    print("내가 지정한 worksheet_name : ", worksheet_name, "=====")
    
    # 리스트에 하나씩 추가 append()하는데
    # 조건이 있어
    # Sale Amount가 2000보다 큰 값 (그 과정에서 $와 ,를 다 ''으로 대체해서 순수한 숫자로 만들어줌)
    row_list.append(data[data['Sale Amount'].replace('$','').replace(',','').astype(float) > threshold])

# axis=0 : row로 추가
# axis=1 : column으로 추가 (이렇게 설정하면, column위치가 sheet별로 다르게 출력됨)
filtered_row = pandas.concat(row_list, axis=0, ignore_index=True)

writer = pandas.ExcelWriter(outputFile)
filtered_row.to_excel(writer, sheet_name="set_of_worksheets", index=False)

writer.save()

