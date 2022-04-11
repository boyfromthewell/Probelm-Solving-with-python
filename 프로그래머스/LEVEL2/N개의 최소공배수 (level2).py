from math import gcd

def solution(num):
  answer=num[0]
  # num[0]과 num[1]의 최소 공부수 구한후 answer에 저장
  for i in num:
    # 차례로 하나씩 증가시키며 최소 공배수 구해주기
    answer=answer*i//gcd(answer,i)
    # 최소공배수=(x*y)//gcd(x,y)
  return answer