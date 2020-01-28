'''
Created on 2020. 1. 28.
@author: GDJ19

    <xls 파일 읽고 쓰기>
    - 쓰기 : pip install xlwt
'''

from xlrd import open_workbook
from xlwt import Workbook

input_file = "ssec1804.xls"
output_file = "ssec1804_out.xls"

# 출력할 excel파일
# 저장이 될 빈 excel파일을 만들었다고 보면 됨
output_workbook = Workbook()

# 위에 만든 빈 excel파일에
# add_sheet("전체증감") : sheet 추가
output_sheet = output_workbook.add_sheet("전체증감")

# workbook : excel 파일
with open_workbook(input_file) as workbook :
    # worksheet는 읽어들인 excel파일(ssec1804.xls)의 1.전체증감 sheet를 가지고 있음
    worksheet = workbook.sheet_by_name("1.전체증감")
    # 선택된 sheet의 row의 개수만큼 반복
    for row_index in range(worksheet.nrows) :
        # 선택된 sheet의 column의 개수만큼 반복
        for column_index in range(worksheet.ncols) :
            
            # 위에서 만든 빈 excel파일에 write
            output_sheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
            print(worksheet.cell_value(row_index, column_index))

# output_sheet를 worksheet를 output_file에 저장하기
output_workbook.save(output_file)