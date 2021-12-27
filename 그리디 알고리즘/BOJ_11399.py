n=input()
data=list(map(int, input().split()))

data.sort()
time_sum=0
sum_list=[]
for i in data:
  time_sum+=i
  sum_list.append(time_sum)
print(sum(sum_list))