INF=int(1e9)

# 노드의 개수 및 간선의 개수 입력 받기
n=int(input())
m=int(input())
# 2차원 리스트를 만들고, 모든값 무한으로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0
# 각 간선에 대한 정보 입력 받아, 그 값으로 초기화
for _ in range(m):
  a,b,c=map(int, input().split())
  graph[a][b]=c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

# 수행 결과 출력
for i in range(1,n+1):
  for j in range(1,n+1):
  # 도달할수 없는 경우
    if graph[i][j]==INF:
      print("INF", end=" ")
   # 도달할수 있는 경우, 거리 출력
    else:
      print(graph[i][j], end=" ")
  print()


