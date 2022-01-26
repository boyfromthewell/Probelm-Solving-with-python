#북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def sol(x,y,direction):
  global answer
  if data[x][y]==0:
    data[x][y]=2
    answer+=1
  for _ in range(4):
    #d가 북쪽을 바라보면 서쪽으로
    #d가 동쪽을 바라보면 북쪽으로
    #d가 남쪽을 바라보면 동쪽으로
    #d가 서쪽을 바라보면 남쪽으로
    new_direction=(direction+3)%4
    nx=x+dx[new_direction]
    ny=y+dy[new_direction]
    if data[nx][ny]==0:
      sol(nx,ny,new_direction)
      return
    direction=new_direction
  # 후진하기
  new_direction=(direction+2)%4
  nx=x+dx[new_direction]
  ny=y+dy[new_direction]
  if data[nx][ny]==1:
    return
  sol(nx,ny,direction)

n,m=map(int,input().split())
x,y,d=map(int,input().split())
data=[]
for _ in range(n):
  data.append(list(map(int, input().split())))

answer=0
sol(x,y,d)
print(answer)