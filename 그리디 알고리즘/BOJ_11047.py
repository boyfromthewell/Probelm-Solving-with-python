n, k = map(int, input().split())
coins=[]
for i in range(n):
  data=int(input())
  coins.append(data)

coins.sort(reverse=True)
count=0

for i in coins:
  if k==0:
    break
  count+=k//i
  k%=i
print(count)