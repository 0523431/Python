'''
Created on 2020. 2. 10.
@author: GDJ19

    <yaml>
    - pip install pyYAML
    - json과 비슷한 문서 저장 방식 / 2001년에 생성됨
'''

import yaml
yaml_str = '''
    Date : 2019-01-03
    PriceList :
        -
            item_id : 1000
            name : Banana
            color : yellow
            price : 800
        -
            item_id : 1001
            name : Orange
            color : orange
            price : 1400
        -
            itme_id : 1002
            name : Apple
            color : red
            price : 2400
'''

# yaml 문서를 파이썬 자료형 Dictionary로 변경
data = yaml.load(yaml_str, Loader=yaml.FullLoader)
print(type(data))
print(data["Date"], "과일가격")
for item in data["PriceList"] :
    print(item["name"], ":", item["color"], "/", item["price"])

print()
customer = [
    {"name" : "Woohyun", "age" : "30", "gender" : "man"},
    {"name" : "Sungkyu", "age" : "32", "gender" : "man"},
    {"name" : "Myungsu", "age" : "29", "gender" : "man"},
    {"name" : "Sungjong", "age" : "28", "gender" : "man"},
    {"name" : "Dongwoo", "age" : "31", "gender" : "man"},
    {"name" : "Sungyeol", "age" : "30", "gender" : "man"}]

# 파이썬 데이터 List를 yaml 문서양식으로 변경하기
# list형태라고 했지만, json형태와 같아 (리스트 안에 dict니까)
yaml_str = yaml.dump(customer)
print(type(yaml_str))
print(yaml_str)


print()
# yaml 문서를 파이썬 자료형 List로 변경
data = yaml.load(yaml_str, Loader=yaml.FullLoader)
for d in data :
    print(d["name"], d["age"], d["gender"])
    
    
    