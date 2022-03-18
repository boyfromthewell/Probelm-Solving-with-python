import sys
input=sys.stdin.readline

n=int(input())
num=list(map(int, input().split()))
oper=list(map(int,input().split()))

max_val=-1e9
min_val=1e9

def dfs(depth, total, plus, minus, multiply,divide):
  global max_val, min_val
  if depth==n:
    max_val=max(total, max_val)
    min_val=min(total, min_val)
    return

  if plus:
    dfs(depth+1, total+num[depth], plus-1, minus, multiply, divide)
  if minus:
    dfs(depth+1, total-num[depth], plus, minus-1, multiply, divide)
  if multiply:
    dfs(depth+1, total*num[depth], plus, minus, multiply-1, divide)
  if divide:
    dfs(depth+1, int(total/num[depth]), plus, minus, multiply, divide-1)

dfs(1,num[0], oper[0], oper[1],oper[2],oper[3])
print(max_val)
print(min_val)