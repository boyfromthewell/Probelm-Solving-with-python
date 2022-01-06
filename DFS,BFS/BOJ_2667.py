from collections import deque

data=[]
n=int(input())
#정보 입력
for _ in range(n):
  data.append(list(map(int, input())))

#방향 설정 (상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):

  queue=deque()
  queue.append((x,y))
  data[x][y]=0
  cnt=1

  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n and data[nx][ny]==1:
        # 탐색 중 1인 부분 0으로 바꿔 다시 방문 X하도록 하기
        data[nx][ny]=0
        queue.append((nx,ny))
        cnt+=1

  return cnt

count_list=[]
for i in range(n):
  for j in range(n):
    if data[i][j]==1:
      count_list.append(bfs(i,j))

count_list.sort()
print(len(count_list))
#print(count_list)
for i in range(len(count_list)):
  print(count_list[i])
