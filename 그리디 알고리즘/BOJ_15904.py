n=input()

data=['U','C','P','C']

#n값과 data의 값을 비교하면서 하나라도 있으면 data에서 제거
for i in n:
  if data:
    if i == data[0]:
      del data[0]
  else:
    break
#data=0이라는것은 UCPC가 다 포함 됬다는 뜻
if len(data)==0:
  print("I love UCPC")
else:
  print('I hate UCPC')