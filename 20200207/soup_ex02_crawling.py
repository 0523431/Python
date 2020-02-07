'''
Created on 2020. 2. 7.
@author: GDJ19

    <crawling>
    - 진짜 크롤링을 해보자
'''

# html 분석 모듈
from bs4 import BeautifulSoup
# url 사용 모듈 (인터넷과 연결해줌)
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp" # 기상청에서 제공하는 xml형식의 파일
# res : url이 제공하는 정보를 가지고 있음 (url을 통해 전달받은 데이터로써 soup의 분석 대상이 됨)
res= req.urlopen(url)
soup = BeautifulSoup(res, "html.parser") # BeautifulSoup 객체

# title태그의 내용 (.도 없고 #도 없음 == 태그를 의미함)
# .string : 태그제외, 문자열만 저장됨
title = soup.find("title").string
wf = soup.find("wf").string

print(title)
print(wf)

'''
    <xml용어>
    - <![CDATA[ 내용  ]] : (c-data) : 문자열
'''