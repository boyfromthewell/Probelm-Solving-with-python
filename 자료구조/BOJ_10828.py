from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
q=deque()
for _ in range(n):
  cmd=input().split()
  if cmd[0]=="push":
    q.append(cmd[1])
  elif cmd[0]=="pop":
    if len(q)==0:
      print(-1)
    else:
      print(q.pop())
  elif cmd[0]=="size":
    print(len(q))
  elif cmd[0]=="empty":
    if q:
      print(0)
    else:
      print(1)
  elif cmd[0]=="top":
    if len(q)==0:
      print(-1)
    else:
      print(q[-1])