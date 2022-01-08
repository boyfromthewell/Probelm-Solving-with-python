n=int(input())

data=[]
for i in range(n):
  input_data=input().split()
  #이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
  data.append((input_data[0], int(input_data[1])))

#점수 기준으로 정렬
data=sorted(data, key=lambda student: student[1])

for student in data:
  print(student[0], end=" ")
