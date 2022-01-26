import sys
#데이터의 개수 셀때 유용한 모듈
from collections import Counter

n=int(sys.stdin.readline())
data=[]
for _ in range(n):
  data.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(data)/n))

# 중앙값
data.sort()
print(data[n//2])

# 최빈값
# 가장 많이 나타나는 값을 맨앞부터 딕셔너리로 순서대로 반환
data2=Counter(data).most_common()
if len(data2)>1 and data2[0][1]==data2[1][1]:
  print(data2[1][0])
else:
  print(data2[0][0])

# 범위
print(max(data)-min(data))