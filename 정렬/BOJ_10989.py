import sys

# input()으로 입력받으면 메모리 초과
n=int(sys.stdin.readline())
data=[0]*10001
#만든 배열에 각 숫자의 개수 넣기
for i in range(n):
  data[int(sys.stdin.readline())]+=1

print(data)
for i in range(10001):
  if data[i]!=0:
    for j in range(data[i]):
      print(i)