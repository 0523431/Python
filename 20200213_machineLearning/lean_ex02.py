'''
Created on 2020. 2. 13.
@author: GDJ19

    <machine learning>
    - pandas 이용하기
'''

import pandas as pd
from sklearn import svm, metrics

xor_input = [[0,0,0], [0,1,1], [1,0,1], [1,1,0]]

# pandas 자료형으로 변환
xor_df = pd.DataFrame(xor_input)
# 모든행 / 0부터 1열 : 데이터부분으로 추출됨
xor_data = xor_df.loc[:, 0:1]
# 모든행 / 2열 : 정답부분으로 추출됨
xor_label = xor_df.loc[:,2]
# 사이킷런 객체 => 머신러닝 툴
clf = svm.SVC()
# 학습하기 
clf.fit(xor_data, xor_label)
# 평가실행 / 답안지
pre = clf.predict(xor_data)
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 = ", ac_score)


print("test 데이터로 평가하기")
test = [[0,0],[1,1], [1,0], [0,1], [1,0], [1,1]] # 테스트 데이터가 중요함
pre = clf.predict(test) # 평가실행 / 답안지
ans = [0, 0, 1, 1, 1, 0]
ac_score = metrics.accuracy_score(ans, pre)
print("test 정답률 = ", ac_score)
