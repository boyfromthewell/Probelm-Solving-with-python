import heapq

n=int(input())
# 힙에 초기 카드 묶음 모두 삽입
heap=[]
for i in range(n):
  data=int(input())
  heapq.heappush(heap, data)

result=0
#힙에 원소 1개 남을때까지
while len(heap)!=1:
  #가장 작은 2개의 카드 묶음 꺼내기
  one=heapq.heappop(heap)
  two=heapq.heappop(heap)
  #카드 묶음 합쳐 다시 힙에 삽입
  sum_val=one+two
  result+=sum_val
  heapq.heappush(heap,sum_val)

print(result)