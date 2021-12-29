#30의 배수 찾기
n=input()

#30은 10이 배수이기도 하면서 3의배수

#10의 배수는 마지막 자리가 0으로 끝나야 함으로 0이업삳면 바로 -1 출력
if "0" not in n:
  print("-1")

#각자리수의 합이 3의 배수이면 3의 배수
else:
  sum_val=0
  for i in range(len(n)):
    sum_val+=int(n[i])
  #3의 배수가 아니면 -1 출력
  if sum_val%3!=0:
    print("-1")
  #가장 큰값 내림차순으로 정렬해서 출력
  else:
    sort_num=sorted(n, reverse=True)
    result="".join(sort_num)
    print(result)