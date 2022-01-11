n=int(input())

data=[]
#입력 쪼개서 리스트삽입
for i in str(n):
  data.append(int(i))

data.sort(reverse=True)

for i in data:
  print(i, end="")