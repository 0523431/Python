'''
Created on 2020. 2. 10.
@author: GDJ19
    
    <machine learning>
    # 머신런닝
    # 기계한테 공부를 시키는 것
    # 주차장에서 번호판 읽기
    # 파이썬에서는 한 줄 이면 됨 ---> 공부해야할 데이타와 정답값만 넘겨주면 됨
    # 샘플 데이터를 어떻게 만들어 주는지가 더 중요한 일 (pandas와 numpy를 이용)
    
    <learn>
    - 머신러닝 예제
    - 사이킷런 툴 사용하기
    - pip install sklearn
    
'''

from sklearn import svm # 사이킷런 툴
from pip._internal.cli.cmdoptions import pre
xor_data = [[0,0,0], [0,1,1], [1,0,1], [1,1,0]]
data = [] # 샘플 데이터
label = [] # 결과값

# 샘플 데이터 생성
for row in xor_data :
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q]) # [0,0] [0,1] [1,0] [1,1]
    label.append(r) # 0 1 1 0

clf = svm.SVC() # 머신러닝을 위한 객체
clf.fit(data, label) # 기계를 학습시킴 clf.fit(공부할 데이터, 결과값)

# 평가하기위한 데이터 생성 (테스트 문제)
sample_data = [[1,1], [1,0], [0,1], [1,1], [1,0], [0,0]]

# 평가하기
# pre : 예측되는 결과 ==> 답안지
pre = clf.predict(sample_data)

# 정답지
ans = [0,1,1,0,1,0]

print("예측 결과 :", pre)
ok =0
total =0
for idx, answer in enumerate(ans) :
    p = pre[idx]
    if p ==answer :
        ok +=1
    total +=1

print("정답률(정답개수)", ok, "/", total, "=", ok/total)

