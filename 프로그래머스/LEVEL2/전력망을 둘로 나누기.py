from collections import deque

def bfs(start,visited,graph):
  q=deque([start])
  result=1
  visited[start]=True
  while q:
    now=q.popleft()
    for i in graph[now]:
      if visited[i]==False:
        visited[i]=True
        q.append(i)
        result+=1
        
  return result

def solution(n,wires):
  answer=100
  graph=[[] for _ in range(n+1)]
  for v1,v2 in wires:
    graph[v1].append(v2)
    graph[v2].append(v1)

  for start,cut in wires:
    visited=[False]*(n+1)
    visited[cut]=True # 미리 방문 처리
    result=bfs(start,visited,graph)
    if abs(result-(n-result))<answer:
      answer=abs(result-(n-result))

  return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))