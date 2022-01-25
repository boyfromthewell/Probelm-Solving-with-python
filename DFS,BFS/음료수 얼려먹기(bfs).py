from collections import deque

n,m=map(int,input().split())
data=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(n):
  data.append(list(map(int,input())))

def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  data[x][y]=1

  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if data[nx][ny]==0:
        data[nx][ny]=1
        queue.append((nx,ny))
  return

result=0
for i in range(n):
  for j in range(m):
    if data[i][j]==0:
      bfs(i,j)
      result+=1

print(result)
