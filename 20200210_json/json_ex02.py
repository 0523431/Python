'''
Created on 2020. 2. 10.
@author: GDJ19

    <json내용에서 날짜와 과일의 가격을 화면에 출력하고, 파일에 저장하기>
    - json이라기보다 dictionary
'''

import json

# price 자료형 dict
price = {
    "date" : "2020-02-10",
    "price" : {
        "Apple" : 800,
        "Orange" : 1000,
        "Banana" : 500
        }
    }

# dictionary를 프린트하는 것과 같아
# 날짜 프린트
print("날짜 : ", price["date"])

for p in price["price"].keys() :
    print("%s => %s" % (p, price["price"][p]))

# json형태의 데이터를 파일로 저장
save = json.dump(price, open("json_output2.json", "w"))

# json 인코딩
# infos = json.dumps(price)
# print(infos)