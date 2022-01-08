n,k=map(int,input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

# 첫번째 인덱스 부터 확인, 두배열 원소 최대 k 번 비교
for i in range(k):
  #a의 원소가 b보다 작은 경우
  if a[i]<b[i]:
    a[i],b[i]=b[i],a[i]  #swap
  # a의 원소가 b보다 크거나 같은 경우 break
  else:
    break

print(sum(a))