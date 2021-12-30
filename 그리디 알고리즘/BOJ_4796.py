case=1
while True:
  L, P, V =map(int, input().split())
  if L ==0 and P ==0 and V ==0:
    break
  result=L*(V//P)
  result+=min((V%P), L)
  print(f"Case {case}: {result}")
  case+=1