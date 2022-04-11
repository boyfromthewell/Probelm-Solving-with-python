def solution(num):
  fib_num=[0,1]
  for i in range(2,num+1):
    fib_num.append((fib_num[i-1]+fib_num[i-2])%1234567)

  return fib_num[num]