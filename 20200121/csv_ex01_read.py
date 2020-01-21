'''
Created on 2020. 1. 21.
@author: GDJ19

    <csv 파일 읽기>
'''

# command라인에서 입력값 받기
import sys

input_file = sys.argv[1] # jeju1.csv
output_file = sys.argv[2] # jeju1_back.csv
'''
    c언어와 python에서 sys.argv[0]는 현재 파일
'''

# 파일을 읽는 방법 2
with open(input_file, "r", newline="") as filereader : # 변수 : filereader
    with open(output_file, "w", newline="") as filewriter : # 변수 : filewriter
        header = filereader.readline()
        header = header.strip() # 공백 제거
        print(header)
        header_list = header.split(",")
        print(header_list)
        
        filewriter.write(",".join(map(str, header_list))+"\r\n")
        for row_list in filereader :
            print(type(row_list)) # type : str, 
            filewriter.write(row_list)
            # filewriter.write("".join(map(str,row_list)))
