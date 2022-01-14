n=int(input())
data=[]
for _ in range(n):
  data.append(list(map(int, input().split())))

for i in range(1,n):
  for j in range(i+1):
    # 양 가장자리인 경우 걍 쭉 내려가서 더해주기
    if j==0:
      data[i][j]+=data[i-1][j]
    elif j==i:
      data[i][j]+=data[i-1][j-1]
    # 대각선 겹치는 값은 위층에서 더 큰 값을 더해줌
    else:
      data[i][j]+=max(data[i-1][j-1], data[i-1][j])

#print(data)
print(max(data[-1]))