data=[]
one=0
two=0

for _ in range(9):
  data.append(int(input()))
sum_val=sum(data)

for i in range(8):
  for j in range(i+1, 9):
    # 데이터 합에서 2개 골라 뺏을때 100이면
    if sum_val-(data[i]+data[j])==100:
      one=data[i]
      two=data[j]

# 리스트에서 고른값 제거
data.remove(one)
data.remove(two)
data.sort()

# 오름차순 정렬 후 출력
for i in data:
  print(i)