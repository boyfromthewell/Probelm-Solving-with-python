n=int(input())
data=[]

for _ in range(n):
  data.append(input().split())

# 정렬기준
# 두번째 원소를 기준으로 내림차순 정렬
# 두번쨰 원소가 같으면 세번째 원소를 기준으로 오름차순 정렬
# 세번째 원소가 같으면 네번째 원소를 기분으로 내림차순 정렬
# 네번째 원소가 같으면 첫번째 원소를 기준으로 오름차순 정렬
data.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in data:
  print(i[0])