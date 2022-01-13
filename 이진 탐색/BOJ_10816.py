from bisect import bisect_left, bisect_right

def count_by_val(x,left_value,right_value):
  right_idx=bisect_right(x,right_value)
  left_idx=bisect_left(x,left_value)
  return right_idx-left_idx

n=int(input())
data=list(map(int,input().split()))
data.sort()
m=int(input())
target_data=list(map(int,input().split()))

for i in target_data:
  print(count_by_val(data,i,i), end=" ")