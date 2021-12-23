#이코테 책 313p
s=input()
count0=0 #모두 0으로 바꾸는 경우
count1=0 #모두 1로 바꾸는 경우

if s[0]=='1': #첫번째 index에 대해 수행
  count0+=1
else:
  count1+=1

for i in range(len(s)-1):
  if s[i]!=s[i+1]:
    #다음 수에서 1로 바뀌는 경우
    if s[i+1]=='1':
      count0+=1
    #다음 수에서 0으로 바뀌는 경우
    else:
      count1+=1
print(min(count0, count1))
