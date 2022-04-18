import sys
input=sys.stdin.readline

n=int(input())
data=[]
rank=[]
result=0
for _ in range(n):
  data.append(int(input()))
for i in range(1,n+1):
  rank.append(i)

data.sort()

for i in range(len(data)):
  result+=abs(data[i]-rank[i])

print(result)