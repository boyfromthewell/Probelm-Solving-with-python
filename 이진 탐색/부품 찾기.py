def binary_search(array, target, start, end):
  while start<=end:
    mid=(start+end)//2
    if array[mid]==target:
      return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]>target:
      end=mid-1
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
      start=mid+1
  return None


n=int(input())
data=list(map(int, input().split()))
data.sort()

m=int(input())
target_data=list(map(int, input().split()))

#손님이 요청한 부품 번호 하나씩 확인
for i in target_data:
  # 해당 부품 존재 확인
  result=binary_search(data,i,0,n-1)
  if result!=None:
    print('yes', end=" ")
  else:
    print('no', end=" ")