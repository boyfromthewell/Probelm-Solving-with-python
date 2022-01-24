from collections import deque
import sys

def bfs(start):
  queue=deque()
  queue.append(start)
  visit[start]=1
  cnt=0

  while queue:
    node=queue.popleft()
    for i in data[node]:
      if visit[i]==0:
        visit[i]=1
        cnt+=1
        queue.append(i)
  return cnt

t=int(input())

for _ in range(t):
  n,m=map(int,sys.stdin.readline().split())
  data=[[] for _ in range(n+1)]
  visit=[0]*(n+1)

  for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    data[x].append(y)
    data[y].append(x)

  result=0
  for i in range(n):
    if visit[i]==0:
      result+=bfs(i)
  print(result)
