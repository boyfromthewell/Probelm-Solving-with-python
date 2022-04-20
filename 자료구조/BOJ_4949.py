import sys
input=sys.stdin.readline

while True:
  s=input().rstrip()
  stack=[]
  if s==".":
    break
    
  flag=True
  for i in s:
    if i=="(" or i=="[":
      stack.append(i)
    elif i==")":
      if len(stack)==0 or stack[-1]=="[":
        flag=False
        break
      elif stack[-1]=="(":
        stack.pop()
    elif i=="]":
      if len(stack)==0 or stack[-1]=="(":
        flag=False
        break
      elif stack[-1]=="[":
        stack.pop()

  if flag and len(stack)==0:
    print("yes")
  else:
    print("no")