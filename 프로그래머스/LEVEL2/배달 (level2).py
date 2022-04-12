INF=int(1e9)

def solution(N,road,K):
  
  graph=[[INF]*(N+1) for _ in range(N+1)]
  answer=0
  # 자기 자신으로 가는 비용은 0으로 초기화
  for i in range(1,N+1):
    for j in range(1,N+1):
      if i==j:
        graph[i][j]=0
        
  for i in road:
    a,b,cost=i
    # 중복된 경로는 작은 값으로 넣어주기
    if cost<graph[a][b]:
      graph[a][b]=cost
      graph[b][a]=cost
      
  # 플로이드 워셜 알고리즘 수행  
  for k in range(1,N+1):
    for a in range(1,N+1):
      for b in range(1,N+1):
        graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

  # 1번 마을에서 각 마을마다 최단거리 탐색
  for i in graph[1]:
    # K이하의 비용이 들면 answer+1
    if i<=K:
      answer+=1
  return answer
