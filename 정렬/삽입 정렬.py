a=[7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(a)):
  for j in range(i,0,-1):
    if a[j]<a[j-1]:# 한칸씩 왼쪽으로 이동
      a[j],a[j-1]=a[j-1],a[j] 
    else: # 자기보다 작은 데이터를 만나면 그 자리에서 멈춤
      break

print(a)