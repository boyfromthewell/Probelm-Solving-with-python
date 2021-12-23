#이코테 책 100p
n, k=map(int, input().split())
count=0

#n이 k이상이면 k로 계속 나누기
while n>=k:
  #n이 k로 나누어 지지 않으면 나누어 질때까지 1빼기
  while n%k!=0:
    n-=1
    count+=1
  #n이 k로 나눠지므로 나눠주기
  n//=k
  count+=1

#마지막으로 남은수 계속 1빼주기
while n>1:
  n-=1
  count+=1

print(count)