from collections import deque

#나이트가 갈수있는 방향 설정
dx=[-1,-2,-1,-2,1,2,2,1]
dy=[-2,-1,2,1,-2,-1,1,2]

n=int(input())
for _ in range(n):
  l=int(input())
  graph=[]
  for _ in range(l):
    graph.append([0]*l)

  #bfs수행
  queue=deque()
  x,y=map(int, input().split())
  w,z=map(int, input().split())
  queue.append((x,y))

  while queue:
    x,y=queue.popleft()
    # x,y가 목표한 지점에 도달했다면 break
    if x==w and y==z:
      break
    for i in range(8):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=l or ny<0 or ny>=l:
        continue
      if graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))

  print(graph[w][z])

  