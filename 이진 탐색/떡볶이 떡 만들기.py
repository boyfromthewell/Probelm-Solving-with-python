n,m=list(map(int, input().split()))
data=list(map(int, input().split()))

#시작점 끝점 설정
start=0
end=max(data)

# 이진 탐색 수행
result=0
while start<=end:
  total=0
  mid=(start+end)//2
  for i in data:
    # 잘랐을때 떡의 양 계산
    if i>mid:
      total+=i-mid
  # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 탐색)
  if total<m:
    end=mid-1
  # 떡이 양의 충분한 경우 덜자르기(오른쪽 부분 탐색)
  else:
    result=mid # 최대한 덜 잘랐을때가 정답이므로, result에 기록
    start=mid+1

print(result)