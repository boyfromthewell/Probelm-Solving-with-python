n=int(input())
data=[]

for _ in range(n):
  data.append(list(map(int, input().split())))

# 첫번쨰는 게산 x, 두번째 시작부터 빨간집인 경우, 초록집인 경우, 파란집인 경우 계산(그 이전 값들중 같은 색 제외한 min값 더하기)
for i in range(1, n):
  data[i][0]+=min(data[i-1][1],data[i-1][2])
  data[i][1]+=min(data[i-1][0],data[i-1][2])
  data[i][2]+=min(data[i-1][0],data[i-1][1])

print(min(data[-1]))