def solution(a,b):
  result=0
  a.sort()
  b.sort(reverse=True)
  print(a,b)
  for i in range(len(a)):
    result+=a[i]*b[i]

  return result

solution([1,4,2],[5,4,4])