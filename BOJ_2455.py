answer=0
data=[]
for _ in range(4):
  a,b=map(int,input().split())
  answer=answer-a+b
  data.append(answer)

print(max(data))
