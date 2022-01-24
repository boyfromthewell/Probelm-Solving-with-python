from collections import deque

m,n,k=map(int,input().split())

graph=[[0]*n for _ in range(m)]
# 상하좌우
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(graph,x,y):
  queue=deque()
  queue.append((x,y))
  graph[x][y]=1
  cnt=1

  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=m or ny<0 or ny>=n:
        continue
      if graph[nx][ny]==0:
        graph[nx][ny]=1
        queue.append((nx,ny))
        cnt+=1
  return cnt

#예시로 있는 그래프를 위로 뒤집은 형태로 만듬
for _ in range(k):
  x1,y1,x2,y2=map(int,input().split())
  for i in range(y1,y2):
    for j in range(x1,x2):
      graph[i][j]=1

result=[]
for i in range(m):
  for j in range(n):
    if graph[i][j]==0:
      result.append(bfs(graph,i,j))

print(len(result))
result.sort()
for i in result:
  print(i, end=" ")