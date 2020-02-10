'''
Created on 2020. 2. 10.
@author: GDJ19

    <json>
    - 문자열 데이터를 json 파일로 파싱하여 결과 조회하기
'''

import json
str = '''
    {
    "date" : "2020-02-10",
    "price" : {
        "Apple" : 800,
        "Orange" : 1000,
        "Banana" : 500
        }
    }
'''

# json.loads : 문자열 정볼르 json 파일로 파싱
price = json.loads(str)

# 날짜 프린트
print("날짜 : ", price["date"])

for p in price["price"].keys() :
    print("%s => %s" % (p, price["price"][p]))

# json형태의 데이터를 파일로 저장
save = json.dump(price, open("json_output3_str.json", "w"))