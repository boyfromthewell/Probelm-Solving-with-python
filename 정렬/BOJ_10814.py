import sys
n=int(sys.stdin.readline())
data=[]

for _ in range(n):
  data.append(sys.stdin.readline().split())

data.sort(key=lambda x: (int(x[0])))

for i,j in data:
  print(i,j)