'''
Created on 2020. 2. 13.
@author: GDJ19

    <붓꽃 데이터 pandas를 이용>
    - pandas를 이용하여 학습데이터와 테스트 데이터 분류하기
'''

import pandas as pd
from sklearn import svm, metrics
# 학습데이터와 테스트 데이터를 분류하기 위한 모듈
from sklearn.model_selection import train_test_split

# pandas로 읽으면 첫 줄을 column로 인식해서 별도로 delete 할 필요 없음
csv = pd.read_csv("iris.csv")
# column의 이름으로
# data 부분을 저장하고,
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
# 정답 부분을 저장함
csv_label = csv["Name"]

# test_size의 비율로 학습 데이터와 테스트 데이터를 나눔
# 즉, 30%만 테스트 데이터로 사용하겠다
train_data, test_data, train_label, test_label = \
                    train_test_split(csv_data, csv_label, test_size=0.3)
print(len(train_data), len(test_data))

# 머신러닝을 위한 객체 
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print("정답률 = ", ac_score)
