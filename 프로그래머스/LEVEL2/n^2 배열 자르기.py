def solution(n,left,right):
  answer=[]
  for i in range(left, right+1):
    # 해당 위치값 = max(해당위치//n, 해당위치 % n) + 1
    answer.append(max(i//n, i%n)+1)
  return answer
print(solution(4,7,14))