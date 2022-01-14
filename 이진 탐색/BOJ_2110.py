n,c=map(int,input().split())

data=[]
for _ in range(n):
  data.append(int(input()))

data.sort()

start=1
# 집 사이 최소 최대거리 계산
end=data[-1]-data[0]
result=0

while(start<=end):
  mid=(start+end)//2
  value=data[0]
  count=1
  for i in range(1,n):
    if data[i]>=value+mid:
      value=data[i]
      count+=1
  # c개 이상의 공유기 설치할수 있는경우 범위 증가
  if count>=c:
    start=mid+1
    result=mid
  # c개 미만이면 거리를 감소
  else:
    end=mid-1
print(result)