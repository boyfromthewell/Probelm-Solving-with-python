k,n=map(int,input().split())
data=[]
for _ in range(k):
  data.append(int(input()))

#시작길이 설정
start=1
end=max(data)

while start<=end:
  mid=(start+end)//2
  #print(mid)
  sum_val=0
  for i in data:
    sum_val+=i//mid #분할된 렌선 수

  if sum_val>=n: #필요한 개수 보다 넘치면 자르는 값 줄여줌
    start=mid+1
  else:
    end=mid-1

print(end)