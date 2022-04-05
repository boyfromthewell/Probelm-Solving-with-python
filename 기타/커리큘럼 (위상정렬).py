from collections import deque
import copy

v=int(input())
# 모든 노드에 대한 진입차수 0으로 초기화
indegree=[0]*(v+1)
graph=[[] for i in range(v+1)]
# 각 각의 시간을 0으로 초기화
time=[0]*(v+1)

# 방향 그래프의 모든 간선정보 입력받기
for i in range(1,v+1):
  data=list(map(int,input().split()))
  time[i]=data[0]
  for x in data[1:-1]:
    indegree[i]+=1
    graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
  result=copy.deepcopy(time)
  q=deque()

  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    for i in graph[now]:
      result[i]=max(result[i], result[now]+time[i])
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)

  for i in range(1,v+1):
    print(result[i])

topology_sort()
    