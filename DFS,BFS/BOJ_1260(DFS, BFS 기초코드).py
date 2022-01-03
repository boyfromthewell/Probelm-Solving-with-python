from collections import deque

def DFS(v):
  #현재 노드 방문처리
  visit_list[v]=1
  print(v, end=" ")
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in range(1, n+1):
    if visit_list[i]==0 and graph[v][i]==1:
      DFS(i)

def BFS(start):
  #들려야 할 정점 저장
  queue=deque()
  queue.append(start)
  visit_list2[start]=1
  
  while queue:
    start=queue.popleft()
    print(start, end=" ")
    for i in range(1, n+1):
      if visit_list2[i]==0 and graph[start][i]==1:
        queue.append(i)
        visit_list2[i]=1

n, m, v =map(int, input().split())

graph=[[0] * (n+1) for _ in range(n+1)]
visit_list=[0]*(n+1)
visit_list2=[0]*(n+1)

for _ in range(m):
  a,b=map(int, input().split())
  graph[a][b]=graph[b][a]=1

DFS(v)
print()
BFS(v)