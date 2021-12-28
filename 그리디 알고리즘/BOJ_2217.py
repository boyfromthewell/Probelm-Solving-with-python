'''
로프 병렬로 연결하면 각 로프에는 w/k만큼의 동일한 중량 걸림

즉 가장 작은 무게를 들수 있는 로프가 들수 있는 질량 * 병렬 로프갯수=최종 무게

우선 로프 내림차순으로 정렬
ex. [100, 80, 60, 40, 20] 이 있다면 [100*1, 80*2, 60*3, 40*4, 20*5]
여기서 가장 큰 값이 답
'''
n=int(input())
data=[]

for _ in range(n):
  data.append(int(input()))

data.sort(reverse=True)
for i in range(n):
  data[i]*=i+1
result=max(data)
print(result)