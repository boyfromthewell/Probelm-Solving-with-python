import sys

t=int(sys.stdin.readline())

for i in range(t):
  cnt=1
  data=[]
  n=int(sys.stdin.readline())
  
  for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    data.append([a,b])
  data.sort()
  max_val=data[0][1]
  
  for j in range(1,n):
    if max_val>data[j][1]:
      cnt+=1
      max_val=data[j][1]

  print(cnt)