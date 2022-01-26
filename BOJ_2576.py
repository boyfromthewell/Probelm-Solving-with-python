data=[]
odd=[]
for _ in range(7):
  data.append(int(input()))

for i in data:
  if i%2!=0:
    odd.append(i)

if len(odd)==0:
  print(-1)
else:
  print(sum(odd))
  print(min(odd))