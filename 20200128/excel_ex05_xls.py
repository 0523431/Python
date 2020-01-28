'''
Created on 2020. 1. 28.
@author: GDJ19

    <문제>
    - ssec1804.xls파일에서 "1.남자", "1.여자" sheet를 선택하여 남자, 여자 ssec1804_mf.xls로 저장하기
'''

from xlrd import open_workbook
from xlwt import Workbook

# 공통된 내용을 함수로 만들자
def makesheet(output_sheet) :
    for row_index in range(worksheet.nrows) :
        for column_index in range(worksheet.ncols) :
            output_sheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))


input_file = "ssec1804.xls"
output_file = "ssec1804_mf.xls"

output_workbook = Workbook()

out_sheet_m = output_workbook.add_sheet("남자")
out_sheet_f = output_workbook.add_sheet("여자")

# with open_workbook(input_file) as workbook :
#     worksheet = workbook.sheet_by_name("1.남자")
#     for row_index in range(worksheet.nrows) :
#         for column_index in range(worksheet.ncols) :
#             out_sheet_m.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
# 
# with open_workbook(input_file) as workbook :
#     worksheet = workbook.sheet_by_name("1.여자")
#     for row_index in range(worksheet.nrows) :
#         for column_index in range(worksheet.ncols) :
#             out_sheet_f.write(row_index, column_index, worksheet.cell_value(row_index, column_index))


# 작업 내용이 반복되니까 함수로 만들어보자
with open_workbook(input_file) as workbook :
    worksheet = workbook.sheet_by_name("1.남자")
    makesheet(out_sheet_m)
    worksheet = workbook.sheet_by_name("1.여자")
    makesheet(out_sheet_f)

output_workbook.save(output_file)