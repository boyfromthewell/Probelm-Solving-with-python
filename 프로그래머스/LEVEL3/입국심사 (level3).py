def solution(n, times):
  answer = 0
  left=min(times)
  right=max(times)*n

  while left<=right:
    mid=(left+right)//2
    cnt=0
    for time in times:
      cnt+=mid//time
      # 모든 심사관 거치지 않아도 mid분 동안 n명이사으이 심사 가능하다면 break
      if cnt>=n:
        break
    # 심사한 사람의 수가 n보다 크거나 같은 경우 범위 줄여주기
    if cnt>=n:
      answer=mid
      right=mid-1
    # 심사한 사람의 수가 n보다 모자란 경우 범위 늘려주기
    elif cnt<n:
      left=mid+1

  return answer


print(solution(6,[7,10]))