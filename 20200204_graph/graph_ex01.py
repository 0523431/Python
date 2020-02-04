'''
Created on 2020. 2. 4.
@author: GDJ19

    <그래프 그리기>
    - ggplot 모듈을 이용해서 그래프를 그려보자
'''

# pip install ggplot
import matplotlib.pyplot as plt

# ggplot 모듈을 이용해서 그래프를 그림
plt.style.use("ggplot")

# 리스트
customers = ["JAVA", "JSP", "SPRING", "HADOOP", "PYTHON"]

# len(customers) : 5
# range(len(customers)) : range(0,5) ==> 즉, 0-4
# 범위
customers_index = range(len(customers))
print(type(customers_index)) # 자료형 range

# 실제 데이터 값 list 설정
sale_amounts = [69,90,85,60,95]

# 그래프 공간(빈 도화지)
fig = plt.figure()
# 1행 1열 1번째 그래프
ax1 = fig.add_subplot(1,1,1)
# 막대 그래프 그리기
# (x축 값, 데이터 값=y축, 위치, 색상)
ax1.bar(customers_index, sale_amounts,align="center",color="lightgreen")
# x축 설정
ax1.xaxis.set_ticks_position("bottom")
# y축 설정
ax1.yaxis.set_ticks_position("left")

# x축 표시 설정
plt.xticks(customers_index, customers, rotation=0, fontsize="small")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("Class Score")

# 이미지로 저장하기
plt.savefig("bar_plot.png", dpi=400, bbox_inches="tight")
# 화면에 이미지 출력하기
plt.show()