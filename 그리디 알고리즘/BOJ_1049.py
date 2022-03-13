n,m=map(int, input().split())
pack=[]
one=[]

for _ in range(m):
  a,b=map(int, input().split())
  pack.append(a)
  one.append(b)

min_pack=min(pack)
answer=0

while n>0:
  if n>=6:
    min_one=min(one)*6
    n-=6
  else:
    min_one=min(one)*n
    n-=n
  if min_one<min_pack:
    answer+=min_one
  else:
    answer+=min_pack
    
print(answer)
    