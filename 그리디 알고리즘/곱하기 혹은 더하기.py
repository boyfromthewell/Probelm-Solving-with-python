#이코테 책 312p
data=input()
result=int(data[0]) #index 0 추출

for i in range(1, len(data)):
  num=int(data[i])
  if num<=1 or result<=1: # 두수 중 하나라도 0 or 1이면 곱하기보다는 더하기 수행
    result+=num
  else:
    result*=num
print(result)