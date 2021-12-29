a, b=map(int, input().split())
count=1
while True:
  # a=b면 while문 break
  if b==a:
    break
  # b가 2로 나누어떨어지지 않으며 마지막 자리 숫자 1 아니거나 b가 a보다 작다면 -1
  elif (b%2!=0 and b%10!=1) or (b<a):
    count=-1
    break
  else:
    #만약 마지막 숫자 1이면 1제거
    if b%10==1:
      b//=10
      count+=1
    #2로 나누어 떨어지면 2로 나누기
    else:
      b//=2
      count+=1

print(count)