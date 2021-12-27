n=int(input())
data=[]
for _ in range(n):
  first,second=map(int, input().split())
  data.append([first, second])

data=sorted(data, key=lambda a:a[0]) # 시작시간을 기준으로 정렬
#print(data)
data=sorted(data, key=lambda a:a[1]) # 끝나는 시간을 기준으로 한번 더 정렬
#print(data)

last=0
count=0
# 시작 시간이 last값보다 크거나 같을 경우 count+1
for i, j in data:
  if i>=last:
    count+=1
    last=j
print(count)