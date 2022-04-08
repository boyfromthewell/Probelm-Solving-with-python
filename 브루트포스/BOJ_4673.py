def solution(n):
  n=n+sum(map(int,str(n)))
  return n

# 셀프 넘버가 아닌수들이 들어갈 집합
notSelfnum=set()

# 셀프 넘버 아닌 수들 넣어주기
for i in range(1,10001):
  notSelfnum.add(solution(i))

# 셀프 넘버 출력
for i in range(1,10001):
  if i not in notSelfnum:
    print(i)
    