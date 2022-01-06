from collections import deque

m, n= map(int, input().split())
graph=[]

# 방향 설정 (상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#토마토 정보 입력 받기
for _ in range(n):
  graph.append(list(map(int, input().split())))

queue=deque()

#토마토 위치좌표 큐에 append
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      queue.append((i,j))

def bfs():
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
        #익히고 1을 더해주면서 횟수 세어주기
        #여기서 나온 제일 큰 답이 정답
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))

bfs()
result=0
for i in graph:
  for j in i:
    #다 찾아봤는데 안익은 토마토가 존재하면 -1
    if j==0:
      print(-1)
      exit(0)
  result=max(result, max(i))
print(result-1)
