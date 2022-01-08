a=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start, end):
  if start>=end: # 원소가 1개이면 종료
    return
  pivot=start # 피벗은 첫번째 원소
  left=start+1
  right=end
  while left<=right:
    #피벗보다 큰데이터 찾을때까지 반복
    while left<= end and array[left]<=a[pivot]:
      left+=1
    #피벗보다 작은 데이터 찾을때까지 반복
    while right>start and array[right]>=array[pivot]:
      right-=1
    # 엇갈렷다면 작은데이터와 피벗 교체
    if left>right:
      array[right], array[pivot]=array[pivot], array[right]
    # 엇갈리지 않았다면 작은데이터와 큰데이터 교체
    else:
      array[left], array[right]=array[right], array[left]
  #분할이후 왼쪽 부분 오른쪽부분 재귀 수행
  quick_sort(array,start, right-1)
  quick_sort(array, right+1, end)

quick_sort(a,0,len(a)-1)
print(a)