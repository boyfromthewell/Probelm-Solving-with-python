import sys
sys.setrecursionlimit(10**7)

n,m=map(int, input().split())
data=[]
temp=[[0]* m for _ in range(n)] # 벽 설치한뒤에 맵 리스트

for _ in range(n):
  data.append(list(map(int, input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
result=0
# dfs이용 바이러스가 사방으로 퍼지도록 하기
def virus(x,y):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx>=0 and nx<n and ny>=0 and ny<m:
      if temp[nx][ny]==0:
        # 해당위치에 바이러스 배치하고 다시 재귀수행
        temp[nx][ny]==2
        virus(nx,ny)
# 안전영역크기 계산하는 함수
def getScore():
  score=0
  for i in range(n):
    for j in range(m):
      if temp[i][j]==0:
        score+=1
  return score

#깊이 우선 탬색을 이용해 울타리 설치하면서, 매번 안전영역의 크기 계산
def dfs(count):
  global result
  # 울타리가 3개 설치된 경우
  if count==3:
    for i in range(n):
      for j in range(m):
        temp[i][j]=data[i][j]
    #각 바이러스 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j]==2:
          virus(i,j)
    # 안전영역의 최댓값 계산
    result=max(result, getScore())
    return 
  # 빈공간에 울타리 설치하기
  for i in range(n):
    for j in range(m):
      if data[i][j]==0:
        data[i][j]=1
        count+=1
        dfs(count)
        data[i][j]=0
        count-=1

dfs(0)
print(result)
