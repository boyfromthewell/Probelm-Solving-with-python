from collections import deque

n,k=map(int, input().split())
graph=[]
data=[]

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    # 해당위치에 바이러스가 존재하는 경우
    if graph[i][j]!=0:
      #바이러스 종류, 시간, 위치 x,y 삽입
      data.append((graph[i][j],0,i,j))

#정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식 됨)
data.sort()
queue=deque(data)

target_s, target_x, target_y=map(int, input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# bfs 수행
while queue:
  virus, s, x, y=queue.popleft()
  if s==target_s:
    break
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    #아직 방문하지 않았다면 그 위치에 바이러스 넣기
    if 0<=nx and nx<n and 0<=ny and ny<n and graph[nx][ny]==0:
      graph[nx][ny]=virus
      queue.append((virus,s+1,nx,ny))

print(graph[target_x-1][target_y-1])