'''
Created on 2020. 1. 21.
@author: GDJ19

    <파일 존재 여부 확인 하기>
'''

import os.path

file = "C:\\Data\\Python\\nofile.txt" # nothing
file = "csv_ex02_read.py" # Yes. It is a file
file = "../20200120"

if os.path.isfile(file) :
    print("Yes. It is a file")
elif os.path.isdir(file) :
    print("Yes. It is a directory")
    
if os.path.exists(file) :
    print("Something exits")
else :
    print("Nothing")
