n=int(input())
zero=[1,0,1] # 0 호출 회수
one=[0,1,1] # 1 호출 회수

def sol(num):
  length=len(zero)
  if length<=num:
    for i in range(length, num+1):
      zero.append(zero[i-1]+zero[i-2])
      one.append(one[i-1]+one[i-2])
  print(zero[num], one[num])

for _ in range(n):
  k=int(input())
  sol(k)
