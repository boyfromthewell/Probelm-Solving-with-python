import math

# n을 k진법으로 바꿔 주는 함수
def n_to_k(n,k):
  if k==10:
    return n
  else:
    num=""
    while n:
      num+=str(n%k)
      n=n//k

  # 문자열 뒤집어서 return
  return num[::-1]

# 소수 판별 함수
def PrimeCheck(num):
  if num==0 or num==1:
    return False
  for i in range(2, int(math.sqrt(num))+1):
    if num%i==0:
      return False
  return True
  
def solution(n,k):
  answer=0
  nums=n_to_k(n,k)
  # 조건에 따라 나눠 주기
  result=str(nums).split("0")
  print(result)
  for i in result:
    if i!="" and PrimeCheck(int(i)):
      answer+=1

  return answer