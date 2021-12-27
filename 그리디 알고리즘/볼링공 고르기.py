#이코테 책 314p
n, m=map(int, input().split())
data=list(map(int, input().split()))

a=[0]*11
#각 무게 해당하는 볼링공 개수 카운트
for i in data:
  a[i]+=1

result=0
#1부터 m까지 각 무게 대해 처리
for i in range(1, m+1):
  n-=a[i] # 무게가 i인 볼링공의 개수(A가 선택할수 있는 개수) 제외
  result+=a[i]*n #B가 선택하는 경우의 수와 곱하기
print(result)

