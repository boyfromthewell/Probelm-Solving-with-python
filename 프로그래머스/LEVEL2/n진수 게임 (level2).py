# 숫자 n진수로 변환
def n_to_k(n,num):
  s="0123456789ABCDEF"
  result=""
  if num==0:
    return "0"
  while num>0:
    result=s[num%n]+result
    num=num//n
  return result

def solution(n,t,m,p):
  answer=""
  temp=""

  # 숫자갯수 * 참가인원 만큼 for문
  for i in range(t*m):
    temp+=n_to_k(n,i)
    
  for j in range(p-1, t*m, m):
    answer+=temp[j]

  return answer

print(solution(2,4,2,1))
    