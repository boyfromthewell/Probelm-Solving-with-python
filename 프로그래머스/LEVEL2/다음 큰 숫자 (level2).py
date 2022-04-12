def solution(n):
  answer=0
  cnt1=bin(n).count("1")

  for i in range(n+1,1000001):
    cnt2=bin(i).count("1")
    if cnt1==cnt2:
      answer=i
      break

  return answer