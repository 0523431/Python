'''
Created on 2020. 2. 4.
@author: GDJ19

    <그래프 여러개 작성하기>
    - 

    - pandas : 데이터를 꺼내오는 모듈 (데이터의 구조..?)
    - numpy : 빅데이터 분석시 많이 사용하는 모듈..
              python에서 사용되는 리스트 형태의 수치 처리 모듈
'''

import numpy as np
import matplotlib.pyplot as plt

# fig : figure 도화지
# 도화지를 2행 2열로 나눠서 사용하겠다
# ax_lst는 그래프 리스트를 의미함
fig, ax_lst = plt.subplots(2, 2, figsize=(8,5))
fig.suptitle("figure sample plots")

# 첫번째 그래프 : 0의 값 1, 1의 값 2, 2의 값 3, 3의값 4
ax_lst[0][0].plot([1,2,3,4])
# 두번째 그래프  : np모듈의 랜덤값을 가지고 그래프를 그림
ax_lst[0][1].plot(np.random.randn(4,10), np.random.randn(4,10))
# 세번째 그래프 : 0부터 5까지, 코사인값을 이용해서.... (수학ㅈㅈ)
ax_lst[1][0].plot(np.linspace(0.0, 5.0), np.cos(2 *np.pi *np.linspace(0.0, 5.0)))
# 네번째 그래프 : x축 =[3,7] / y축 =[5,4]
ax_lst[1][1].plot([3,7], [5,4])

plt.show()