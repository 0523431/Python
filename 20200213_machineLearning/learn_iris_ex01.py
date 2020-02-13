'''
Created on 2020. 2. 13.
@author: GDJ19

    <붓꽃 데이터 사용하기>
    - https://github.com/pandas-dev/pandas/blob/master/pandas/tests/data/iris.csv
'''

from sklearn import svm, metrics
# 난순발생 모듈 : random
# 정규화관련 모듈 : re
import random, re

csv = []
with open("iris.csv", "r", encoding="UTF-8") as fp :
    # 한 줄을 읽어
    for line in fp :
        line = line.strip() # 공백제거
        cols = line.split(",") # ,로 구분하기 / 단어구분
        
        # 함수
        # <정규식 설명>
        # [0-9\.] : 0부터 9까지의 숫자 또는 .
        # ^ : 시작문자
        # $ : 종료문자
        # + : 1개이상
        # ^[0-9\.]+$ : 숫자나 점으로 이루어져 있음
        # r : row
        # 즉, row 데이터 숫자나 점으로 이루어져있으면 => float(n) : 실수로 변경
        fn = lambda n:float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols) # iris.csc 파일을 자료형에 맞도록 저장

del csv[0] # Header 부분 삭제

# csv 리스트 : 실수형으로 변환된 숫자 data만 저장됨
# csv 섞기
random.shuffle(csv)

# 학습데이터와 평가데이터 분리하기
total_len = len(csv)
train_len = int(total_len * 2/3) # 학습 데이터 개수
train_data =[]  # 학습데이터
train_label =[] # 학습데이터의 정답
test_data =[]   # 테스트 데이터
test_label =[]  # 테스트 데이터의 정답

for i in range(total_len) :
    data = csv[i][0:4]  # 학습데이터
    label = csv[i][4]   # 결과
    if i < train_len :
        train_data.append(data)     # 학습데이터 배열에 저장
        train_label.append(label)   # 결과 저장
    else :
        test_data.append(data)      # 학습 완료 후 평가 데이터로 저장
        test_label.append(label)    # 학습 완료 후 정답데이터로 저장
# 학습데이터와 평가데이터 분리 끝

# 머신러닝을 위한 객체 
clf = svm.SVC()
clf.fit(train_data, train_label) # 기계를 학습시킴
pre = clf.predict(test_data)     # 평가하기

# 정확도 결과 출력
ac_score = metrics.accuracy_score(test_label, pre)
print("정답률 = ", ac_score)