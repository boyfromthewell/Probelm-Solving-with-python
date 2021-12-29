input_data=int(input())

q=0
d=0
n=0
p=0

for _ in range(input_data):
  c=int(input())
  q=c//25
  d=(c%25)//10
  n=(c%25)%10//5
  p=(c%25%10%5)//1
  print(q, d, n, p)