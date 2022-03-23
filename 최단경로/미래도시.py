INF=int(1e9)

# 노드 개수, 간선 개수 입력 받기
n,m=map(int,input().split())
# 2차원 리스트 만들고, 모든값 무한으로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b]=0

for _ in range(m):
  a,b=map(int,input().split())
  #a와 b가 서로에게 가는 비용은 1이라고 설정
  graph[a][b]=1
  graph[b][a]=1

# 목적지 x와 거쳐갈 노드 k 입력 받기
x,k=map(int,input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

# 최단거리 계산
distance=graph[1][k]+graph[k][x]

# 도달 할 수 없는 경우 -1
if distance>=INF:
  print(-1)
# 도달할수 있으면 최단 거리 출력
else:
  print(distance)
