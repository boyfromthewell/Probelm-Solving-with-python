#이코테 책 314p
n=input()
data=list(map(int, input().split()))

target=1
data.sort()
for i in data:
  #만들수 없는 금액 찾았을때 반복 종료
  if target<i:
    break
  target+=i

print(target)
