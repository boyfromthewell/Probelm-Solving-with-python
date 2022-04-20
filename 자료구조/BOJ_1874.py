import sys
input=sys.stdin.readline

n=int(input())
stack=[]
result=[]
flag=True
cnt=1

for _ in range(n):
  num=int(input())
  # 입력한 수 만날때까지 오름차순으로 push
  while cnt<=num:
    stack.append(cnt)
    result.append("+")
    cnt+=1
  if stack[-1]==num: # stack의 top이 입력한 숫자와 같다면
    stack.pop() # 스택의 top을 꺼내 수열을 만들어 주기
    result.append("-")
  else:
    print("NO")
    flag=False
    break
    
if flag:
  for i in result:
    print(i)

