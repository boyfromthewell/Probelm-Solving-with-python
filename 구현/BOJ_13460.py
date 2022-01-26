# 졸라어렵네...

n,m=map(int,input().split())
data=[]
for _ in range(n):
  data.append(list(input()))
visit=[[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

queue=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def pos_init():
  red_x,red_y,blue_x,blue_y=0,0,0,0
  for i in range(n):
    for j in range(m):
      if data[i][j]=='R':
        red_x,red_y=i,j
      elif data[i][j]=="B":
        blue_x,blue_y=i,j
  #위치정보 저장
  queue.append((red_x,red_y,blue_x,blue_y,1))
  visit[red_x][red_y][blue_x][blue_y]=True

def move(x,y,dx,dy):
  cnt=0
  #다음이 벽이거나 현재가 구멍일때까지
  while data[x+dx][y+dy]!='#' and data[x][y]!='O':
    x+=dx
    y+=dy
    cnt+=1
  return x,y,cnt

def solve():
  pos_init()
  while queue:
    red_x,red_y,blue_x,blue_y,depth=queue.pop(0)
    if depth>10:
      break
    for i in range(4):
      nrx,nry,rcnt=move(red_x,red_y,dx[i],dy[i])
      nbx,nby,bcnt=move(blue_x,blue_y,dx[i],dy[i])

      if data[nbx][nby]!='O': # 실패조건이 아니면
        if data[nrx][nry]=='O': # 성공 조건이면
          print(depth)
          return
        if nrx==nbx and nry==nby: # 겹쳤을때
          if rcnt>bcnt: # 이동거리 많은것을
            nrx-=dx[i] # 한칸 뒤로
            nry-=dy[i]
          else:
            nbx-=dx[i]
            nby-=dy[i]
        # 탐색후 탐사여부 체크
        if not visit[nrx][nry][nbx][nby]:
          visit[nrx][nry][nbx][nby]=True
          #다음 depth의 breadth 탐색 위한 큐
          queue.append((nrx,nry,nbx,nby,depth+1))
  print(-1)

solve()