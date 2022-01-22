from collections import deque

def bfs(start):
  queue=deque()
  queue.append(start)
  while queue:
    start=queue.popleft()
    for i in data[start]:
      if visit[i]==0:
        visit[i]=visit[start]+1
        queue.append(i)

n=int(input())
data=[[] for _ in range(n+1)]
s,e=map(int,input().split())

m=int(input())
for _ in range(m):
  x,y=map(int,input().split())
  data[x].append(y)
  data[y].append(x)

visit=[0]*(n+1)
bfs(s)

print(visit[e] if visit[e]>0 else -1)