#이코테 책 96p
n, m=map(int, input().split())
result=0

for i in range(n):
  data=list(map(int, input().split()))
  min_val=min(data) # 현재줄에서 가장 작은수 찾기
  result=max(result, min_val) #가장 작은수 중에 큰값 찾기
print(result)