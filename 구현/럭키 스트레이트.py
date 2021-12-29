#이코테 321p
n=input()

#입력 반으로 나누기
left=n[:len(n)//2]
right=n[len(n)//2:]

left_sum=0
right_sum=0

for i in range(len(n)//2):
  left_sum+=int(left[i])
  right_sum+=int(right[i])

if left_sum==right_sum:
  print("LUCKY")
else:
  print("READY")