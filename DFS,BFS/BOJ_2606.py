n=int(input())
m=int(input())
cnt=0
data=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a,b=map(int, input().split())
  data[a][b]=data[b][a]=1

def dfs(data, v, visited):
  global cnt
  visited[v]=1
  for i in range(n+1):
    if visited[i]==0 and data[v][i]==1:
      dfs(data, i, visited)
      cnt+=1

visited=[0]*(n+1)
dfs(data,1,visited)
print(cnt)