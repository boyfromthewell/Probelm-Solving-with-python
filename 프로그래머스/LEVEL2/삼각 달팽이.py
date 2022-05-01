def solution(n):
  result=[[0]*n for _ in range(n)]
  x,y=-1,0
  num=1
  answer=[]
  for i in range(n): # 방향
    for j in range(i,n):
      if i%3==0: # 아래
        x+=1 
      elif i%3==1: # 오른쪽
        y+=1
      else: # 위로
        x-=1
        y-=1
      result[x][y]=num
      num+=1
  for i in result:
    for j in range(len(i)):
      if i[j]!=0:
        answer.append(i[j])

  return answer

print(solution(4))