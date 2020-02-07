'''
Created on 2020. 2. 7.
@author: GDJ19

    <xml 파일을 읽어 분석하기>
'''

from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# url을 읽자
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
if not os.path.exists("forecast.xml") :
    # url의 내용을 forecast.xml 파일로 저장
    req.urlretrieve(url, "forecast.xml")

# xml파일을 읽어서 xml값에 저장하기
xml = open("forecast.xml", "r", encoding="UTF-8").read()

# dictionary 사용
# 날씨를 구분점으로 해서 도시들을 저장
info = {}
soup = BeautifulSoup(xml, "html.parser")

for location in soup.find_all("location") : # .도 #도 없어 ==> 태그
    name = location.find("city").string
    weather = location.find("wf").string
    
    if not (weather in info) :
        info[weather] = [] # 빈 리스트를 만들고
    info[weather].append(name) # 날씨가 같은 도시를 모을 수 있게 분석

for weather in info.keys() :
    print("+", weather)
    for name in info[weather] :
        print(" |- ", name)

