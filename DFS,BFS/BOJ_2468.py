from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[]
max=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
  graph.append(list(map(int,input().split())))
  for j in range(n):
    if graph[i][j]>max:
      max=graph[i][j] # 그래프에서 최대값 찾기

def bfs(x,y,value,visited):
  q=deque()
  q.append((x,y))
  visited[x][y]=1
  while q:
    x,y=q.popleft()
    
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      
      if 0<=nx<n and 0<=ny<n:
        if graph[nx][ny]>value and visited[nx][ny]==0: # 강수량보다 높은곳만 방문
          visited[nx][ny]=1
          q.append((nx,ny))

result=0
for i in range(max): # 강수량 모두 체크
  visited=[[0] * n for _ in range(n)] # 매 강수량 마다 visited 갱신
  ans=0
  for j in range(n):
    for k in range(n):
      if graph[j][k]>i and visited[j][k]==0:
        bfs(j,k,i,visited)
        ans+=1
  if ans>result:
    result=ans

print(result)