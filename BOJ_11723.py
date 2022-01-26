import sys
s=set() # set 자료형 사용
n=int(sys.stdin.readline())
data=[]

for _ in range(n):
  input_data=sys.stdin.readline().strip().split()

  if len(input_data)==1:
    if input_data[0]=="all":
      s=set([i for i in range(1,21)])
    else:
      s=set()
    continue
  
  command, val=input_data[0], input_data[1]
  val=int(val)

  if command=="add":
    s.add(val)
  elif command=="check":
    print(1 if val in s else 0)
  elif command=="remove":
    s.discard(val)
  elif command=="toggle":
    if val in s:
      s.discard(val)
    else:
      s.add(val)