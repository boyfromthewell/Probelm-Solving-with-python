from itertools import combinations

# 소수 판별 함수
def primeCheck(num):
  if num<2:
    return True
  for i in range(2,num//2+1):
    if num%i==0:
      return False
  return True

def solution(nums):
  result=0
  # 조합 이용 경우의 수 구하기
  for i in list(combinations(nums,3)):
    sum_val=0
    sum_val+=sum(i)
    if primeCheck(sum_val):
      result+=1

  return result
      
print(solution([1,2,3,4]))