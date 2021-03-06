def dfs(n,computers,start,visited):
  visited[start]=True
  for i in range(n):
    if visited[i]==False and computers[start][i]==1:
      dfs(n,computers,i,visited)

def solution(n, computers):
  answer = 0
  visited=[False]*n
  for i in range(n):
    if visited[i]==False:
      dfs(n,computers,i,visited)
      answer+=1
  return answer

print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))