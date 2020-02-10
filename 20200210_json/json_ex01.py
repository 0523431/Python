'''
Created on 2020. 2. 10.
@author: GDJ19
    
    <json>
    - json은 dictionary와 같아
    - 분석 기법은 dictionary
'''

import json
import os.path
import urllib.request as req # 요청 정보

url = "https://api.github.com/repositories"
# url에서 전달된 json파일을 저장
savename = "repo.json"
if not os.path.exists(savename) :
    req.urlretrieve(url, savename)

# json.load : 해당 파일의 내용을 json형태로 파싱해서 json 객체로 저장함 ==> items ==> class 'list' 리스트 타입
# 원래 json파일은 dictionary인데, 파일을 url파일을 열어보면 시작이 [ 이기때문에, list타입이 됨 ==> 리스트 안에 dictionary타입
# (읽을 파일 이름, read, 인코딩 방식)
items = json.load(open(savename, "r", encoding="UTF-8"))
print(type(items)) # list
for item in items :
    print(type(item)) # dictionary
    print(item["name"] + "-" + item["owner"]["login"])

# json.dump : json형태의 데이터를 파일로 저장
json.dump(items, open("json_output.json", "w", encoding="UTF-8"))
