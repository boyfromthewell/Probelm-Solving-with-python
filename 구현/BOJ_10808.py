n=input()

data=[0]*26

for i in n:
  for j in range(len(data)):
    if int(ord(i))-97==j:
      data[j]+=1

for i in data:
  print(i, end=" ")