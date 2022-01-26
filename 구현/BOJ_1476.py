e,s,m,cnt=1,1,1,1

input_e,input_s,input_m=map(int,input().split())

while True:
  if e==input_e and s==input_s and m==input_m:
    break
  e+=1
  s+=1
  m+=1
  cnt+=1
  if e>15:
    e-=15
  if s>28:
    s-=28
  if m>19:
    m-=19

print(cnt)