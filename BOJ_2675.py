t=int(input())

for _ in range(t):
  r,s=input().split()
  result_list=[]
  for i in s:
    result_list.append(i*int(r))
  answer="".join(result_list)
  print(answer)