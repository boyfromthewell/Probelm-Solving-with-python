data=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

n=input()
result=0
for i in range(len(n)):
  for j in data:
    if n[i] in j:
      result+=data.index(j)+3
print(result)