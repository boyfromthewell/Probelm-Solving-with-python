n=int(input())

for _ in range(n):
  s=input()
  cnt=0
  for i in range(len(s)):
    if s[i]=="(":
      cnt+=1
    elif s[i]==")":
      cnt-=1
    if cnt<0:
      print("NO")
      break
  if cnt==0:
    print("YES")
  elif cnt>0:
    print("NO")