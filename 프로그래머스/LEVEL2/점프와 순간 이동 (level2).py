def solution(n):
  answer=0
  while n!=0:
    # n이 짝수로 나눠지면 순간이동
    if n%2==0:
      n//=2
    # 아니면 한칸 이동, 건전지 소모 +1
    else:
      n-=1
      answer+=1

  return answer

print(solution(5000))
    