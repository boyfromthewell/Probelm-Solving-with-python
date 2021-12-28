n=int(input())
charge=1000-n
cnt=0
coins=[500,100,50,10,5,1]

for i in coins:
  if charge>=i:
    cnt+=charge//i
    charge=charge%i
print(cnt)
