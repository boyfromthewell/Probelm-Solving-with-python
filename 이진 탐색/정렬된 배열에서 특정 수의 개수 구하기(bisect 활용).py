from bisect import bisect_left, bisect_right # 찾은 값 왼쪽, 오른쪽 인덱스 반환해줌!!!!!!!!!!

#값이 [left_val, right_val]인 데이터의 개수 반환
def count_by_value(array,left_val,right_val):
  right_index=bisect_right(array,right_val)
  left_index=bisect_left(array,left_val)
  return right_index-left_index

n,x=map(int,input().split())
data=list(map(int,input().split()))

count=count_by_value(data,x,x)

if count==0:
  print(-1)
else:
  print(count)