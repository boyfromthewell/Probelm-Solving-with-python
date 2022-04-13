from itertools import permutations
import math

# 소수 판별 함수
def primeCheck(num):
  if num<2:
    return False
  for i in range(2, int(math.sqrt(num))+1):
    if num%i==0:
      return False
  return True
  
def solution(numbers):
  answer=0
  result=[]
  # 1부터 number의 길이까지 순열 만들기
  for i in range(1,len(numbers)+1):
    temp=list(permutations(numbers,i))
    result+=[int("".join(i)) for i in temp]
  # set으로 중복 제거후 소수 판별
  for num in set(result):
    if primeCheck(num):
      answer+=1

  return answer