from collections import deque

t=int(input())

#방향 설정(상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

######################################
def bfs(graph,x,y):
  queue=deque()
  queue.append((x,y))
  graph[x][y]=0

  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0>nx or nx>=m or 0>ny or ny>=n:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny]=0
        queue.append((nx, ny))
  return
###################################
for _ in range(t):
  cnt=0
  m, n, k= map(int, input().split())

  graph=[[0]*n for _ in range(m)]
  #print(graph)
  for _ in range(k):
    x, y=map(int, input().split())
    graph[x][y]=1

  for i in range(m):
    for j in range(n):
      if graph[i][j]==1:
        bfs(graph,i,j)
        cnt+=1
  print(cnt)