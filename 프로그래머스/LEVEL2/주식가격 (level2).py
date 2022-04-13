from collections import deque

def solution(prices):
  result=[]
  prices=deque(prices)

  while prices:
    cnt=0
    # 맨앞 원소 뽑아내고 삭제
    p=prices.popleft()
    # 나머지 가격들 검사
    for item in prices:
      cnt+=1
      # 가격이 떨어졌으면 중지
      if item<p:
        break
    result.append(cnt)
    
  return result

print(solution([1,2,3,2,3]))