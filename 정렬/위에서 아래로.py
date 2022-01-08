n=int(input())

data=[]
# n 개의 정수 입력받아 리스트에 저장
for _ in range(n):
  data.append(int(input()))

#라이브러리 사용
data=sorted(data,reverse=True)

for i in data:
  print(i, end=" ")
