def solution(number, k):
  answer=[]

  # 큰 수가 앞자리가 되게끔 스택에 저장
  for i in number:
    while answer and answer[-1]<i and k>0:
      answer.pop()
      k-=1
    answer.append(i)
    
  # k가 남았다면 k=0될때까지 뒤에서 뺴주기
  while k>0:
    answer.pop()
    k-=1

  return "".join(answer)
    
print(solution("1924",2))