n=int(input())
cnt=0

if n<10:
  n*=10
result=n

while True:
  num1=result//10
  num2=result%10

  num3=num1+num2

  result=(num2*10)+(num3%10)
  cnt+=1
  if result==n:
    break

print(cnt)