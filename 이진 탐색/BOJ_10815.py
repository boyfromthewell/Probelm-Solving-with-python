def binary_search(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    if array[mid]==target:
      return mid
    elif array[mid]>target:
      end=mid-1
    else:
      start=mid+1

  return None

n=int(input())
data=list(map(int,input().split()))
data.sort()
m=int(input())
target_data=list(map(int,input().split()))

for i in target_data:
  result=binary_search(data,i,0,n-1)
  if result==None:
    print(0, end=" ")
  else:
    print(1, end=" ")