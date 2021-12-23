n, m, k = map(int, input().split())
data=list(map(int, input().split()))

data.sort()
firstBig=data[n-1] # 가장 큰수
secondBig=data[n-2] # 두번째로 큰수

sum=0

while True:
  for i in range(k): #가장 큰수 k번 더하기
    if m==0:
      break
    sum+=firstBig
    m-=1
  if m==0:
    break
  sum+=secondBig
  m-=1

print(sum)

