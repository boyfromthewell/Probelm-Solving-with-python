def binary_search(array,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  # 고정점 찾은 경우 인덱스 반환
  if array[mid]==mid:
    return mid
  # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 출력
  elif array[mid]>mid:
    return binary_search(array,start,mid-1)
  # 중갅머이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
  else:
    return binary_search(array, mid+1, end)

n=int(input())
data=list(map(int, input().split()))

idx=binary_search(data,0,n-1)

if idx==None:
  print(-1)
else:
  print(idx)