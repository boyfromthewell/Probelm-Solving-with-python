graph=[]
for _ in range(5):
  graph.append(list(map(str,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=[]

def dfs(x,y,number):
  number+=graph[x][y]

  if len(number)==6:
    if number not in result:
      result.append(number)
    return 

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if 0<=nx<5 and 0<=ny<5:
      dfs(nx,ny,number)

for i in range(5):
  for j in range(5):
    dfs(i,j,"")

print(len(result))


