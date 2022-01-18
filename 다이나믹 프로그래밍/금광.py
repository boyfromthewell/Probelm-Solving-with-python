t=int(input())
for _ in range(t):
  n,m=map(int,input().split())
  data=list(map(int,input().split()))
  gold=[]
  idx=0
  for _ in range(n):
    gold.append(data[idx:idx+m])
    idx+=m
  #데이터의 위치에 따라 dp테이블 갱신
  for j in range(1,m):
    for i in range(n):
      # 맨 위에 있는 값이라면 왼쪽 값과 대각선 아래 값 비교
      if i==0:
        gold[i][j]=max(gold[i][j-1]+gold[i][j], gold[i+1][j-1]+gold[i][j])
      # 맨아래 값이라면 왼쪽 값과 대각선 위의 값 비교
      elif i==n-1:
        gold[i][j]=max(gold[i][j-1]+gold[i][j], gold[i-1][j-1]+gold[i][j])
      # 중간의 값이면 세 방향 모두 비교
      else:
        gold[i][j]=max(gold[i-1][j-1]+gold[i][j], gold[i][j-1]+gold[i][j],gold[i+1][j-1]+gold[i][j])
  result=0
  for i in gold:
    result=max(result,max(i))
  print(result)
