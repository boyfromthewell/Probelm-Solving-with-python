import sys
input=sys.stdin.readline

INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는비용은 0으로
for i in range(1, n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

for _ in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

# 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])

result=[]
min_val=INF
min_person=0
# 각 유저의 케빈 베이컨의 수를 result에 넣어줌
for i in range(1, n+1):
  sum=0
  for j in range(1,n+1):
    sum+=graph[i][j]
  result.append(sum)

# 가장 작은 케빈 베이컨 수 가진 사람의 인덱스 찾기
for i in range(n):
  if result[i]<min_val:
    min_val=result[i]
    min_person=i

print(min_person+1)
    

