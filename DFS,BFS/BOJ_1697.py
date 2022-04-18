import sys
input=sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
# 움직일수 있는 최대 좌표 100000
max_num=100000
visited=[0]*(max_num+1)

def bfs():
  q=deque()
  # 출발위치 큐에 삽입
  q.append(n)
  
  while q:
    x=q.popleft()
    # 위치가 동생의 위치와 같다면 종료
    if x==k:
      print(visited[x])
      break
    # 이동 할 수 있는 방향 정의
    for i in (x-1,x+1,x*2):
      if 0<=i<=max_num and visited[i]==0:
        visited[i]=visited[x]+1
        q.append(i)

bfs()