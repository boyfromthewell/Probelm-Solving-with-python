import sys
sys.setrecursionlimit(10000)

n,m=map(int, sys.stdin.readline().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visit_list=[0]*(n+1)
cnt=0

def DFS(start):
  visit_list[start]=1
  for i in range(1,n+1):
    if graph[start][i]==1 and visit_list[i]==0:
      DFS(i)

for _ in range(m):
  a,b=map(int,sys.stdin.readline().split())
  graph[a][b]=1
  graph[b][a]=1

for i in range(1,n+1):
  if visit_list[i]==0:
    DFS(i)
    cnt+=1

print(cnt)