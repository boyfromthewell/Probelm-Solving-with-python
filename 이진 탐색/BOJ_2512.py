n=int(input())
data=list(map(int,input().split()))
m=int(input())

start=0
end=max(data)

# 이진 탐색 수행
while start<=end:
  mid=(start+end)//2
  total=0
  for i in data:
    # mid값보다 예산액이 크면 mid값 할당
    if i>mid:
      total+=mid
    # mid가 더 크면 그냥 예산액 할당
    else:
      total+=i
  # 모자르면 범위 늘리기
  if total<=m:
    start=mid+1
  # 지출양이 더크면 범위 줄이기
  else:
    end=mid-1

print(end)
