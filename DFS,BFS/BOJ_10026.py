from collections import deque

data=[]
n=int(input())
#정보 입력
for _ in range(n):
  data.append(list(map(str, input())))

#방향 설정 (상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  visited[x][y]=1
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      #인덱스 범위 안에 있고 같은 색이면서 방문 안한경우
      if 0<=nx<n and 0<=ny<n and data[nx][ny]==data[x][y] and not visited[nx][ny]:
        visited[nx][ny]=1 #방문 체크 후 큐에 삽입
        queue.append((nx,ny))

visited=[[0]*(n+1) for _ in range(n+1)]
cnt=0

#적록색약 아닌 경우
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i,j)
      cnt+=1

#적록색약인경우 데이터 바꿔주기
for i in range(n):
  for j in range(n):
    if data[i][j]=='G':
      data[i][j]='R'

visited=[[0]*(n+1) for _ in range(n+1)]

cnt1=0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i,j)
      cnt1+=1
      
print(cnt, cnt1)