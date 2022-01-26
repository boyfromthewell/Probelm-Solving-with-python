m=int(input())
n=int(input())
data_list=[]
i=1
#i를 제곱하면서 m,n사이에 있는가 검사 있으면 리스트에 넣기
while i**2<=n:
  if m<=i**2<=n:
    data_list.append(i**2)
  i+=1

if len(data_list)==0:
  print(-1)
else:
  print(sum(data_list))
  print(min(data_list))