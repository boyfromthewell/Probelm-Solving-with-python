n=int(input())
digit=[0]*26

# 알파벳 담는 26크기 배열 만들거 현재 알파벳의 자릿수만큼 미리 만든 배열에 더하기
for _ in range(n):
  word_list=list(input())
  for i in range(len(word_list)):
    digit[ord(word_list[i])-65]+=10**(len(word_list)-i-1)

digit.sort(reverse=True)
result=0
d=9
#9부터 차례로 곱해주기
for i in digit:
  if not i:
    break
  result+=i*d
  d-=1

print(result)