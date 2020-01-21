'''
Created on 2020. 1. 21.
@author: GDJ19

    <jeju1.txt 파일 생성하기>
    - euc-kr > utf-8형태로 바꾸기
'''
import codecs

input_file = "jeju1.csv"
output_file = "jeju1.txt"

read_file = codecs.open(input_file, "r", "euc-kr").read()
data = []
rows = read_file.split("\r\n")
for row in rows :
    if row == "" : continue # 입력줄이 공백
    cells = row.split(",") # list형
    data.append(cells)

write_file = open(output_file, "w", encoding="UTF-8")
for cell in data :
    # print(cell[0], cell[1], cell[2])
    write_file.write(" ".join(map(str, cell)) + "\n")

print("파일 생성 완료")