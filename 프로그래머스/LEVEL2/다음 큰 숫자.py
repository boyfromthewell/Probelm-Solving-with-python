def solution(n):
  answer=0

  count1=bin(n).count("1")

  for i in range(n+1, 1000001):
    count2=bin(i).count("1")

    if count2==count1:
      answer=i
      break

  return answer

print(solution(78))
