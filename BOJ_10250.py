t=int(input())

for _ in range(t):
  h,w,n=map(int,input().split())
  y=n%h
  x=n//h+1
  if n%h==0:
    y=h
    x=n//h
  print(y*100+x)