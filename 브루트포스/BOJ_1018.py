n,m=map(int,input().split())
data=[list(input()) for _ in range(n)]
result=[]

for i in range(n-7):
  for j in range(m-7):
    wcnt=0
    bcnt=0
    for k in range(i,i+8):
      for l in range(j,j+8):
        if (k+l)%2==0:
          if data[k][l]!='W': # W로 시작했는데 첫번째가 W가 아니면 다시 칠하기
            wcnt+=1
          if data[k][l]!='B': # B로 시작했는데 첫번째가 B가 아니면 다시 칠하기
            bcnt+=1
        else:
          if data[k][l]!="B": # W로 시작했는데 두번째 글자가 B가 아니면 다시 칠하기
            wcnt+=1
          if data[k][l]!="W": # B로 시작했는데 두번째 글자가 W가 아니면 다시 칠하기
            bcnt+=1
    result.append(wcnt)
    result.append(bcnt)

print(min(result))