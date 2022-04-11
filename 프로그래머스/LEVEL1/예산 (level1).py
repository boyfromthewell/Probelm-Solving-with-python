def solution(d, budget):
  d.sort()
  sum=0
  result=0
  for i in d:
    sum+=i
    if sum<=budget:
      result+=1
    else:
      break

  return result

print(solution([1,3,2,5,4],	9))