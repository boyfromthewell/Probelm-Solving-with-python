import sys
n,m=map(int, sys.stdin.readline().split())
# set 자료형 활용
nohear=set()
nosee=set()

for _ in range(n):
  nohear.add(input())
for _ in range(m):
  nosee.add(input())

# 겹치는 원소 list로 삽입, 정렬
result=sorted(list(nohear&nosee))

print(len(result))
for i in result:
  print(i)