from itertools import combinations

vowels=['a','e','i','o','u']
l,c=map(int,input().split())
data=input().split()
data.sort()

for pwd in combinations(data,l):
  모음cnt=0
  자음cnt=0
  for i in pwd:
    if i in vowels:
      모음cnt+=1
    else:
      자음cnt+=1
  if 모음cnt>=1 and 자음cnt>=2:
    print("".join(pwd))
  