n=int(input())
d=[0]*(n+1) # n개의 최댓값 저장 배열
p=[0]+list(map(int,input().split())) # 입력받는 배열

# 한개 살때 최댓값 p[1]
d[1]=p[1]

"""
d[2] = d[1] + p[1] or d[0] + p[2]
d[3] = d[2] + p[1] or d[1] + p[2] or d[0] + p[3]
d[4] = d[3] + p[1] or d[2] + p[2] or d[1] + p[3] or d[0] + p[4]

이렇게 될 수 있음, []안은 카드 개수 의미
즉 모든 경우의 수 계산해서 최댓값 구하기
"""
for i in range(2,n+1):
  for j in range(1,i+1):
    if d[i]<d[i-j]+p[j]:
      d[i]=d[i-j]+p[j]

#print(d)
#print(p)
print(d[n])
