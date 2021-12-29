#이코테 322p
s=input()
alpha=[]
num_val=0
for i in s:
  if i.isalpha(): # isalpha->알파벳 판별 파이썬 내장함수
    alpha.append(i)
  else:
    num_val+=int(i) # 숫자는 그냥 더해줌

alpha.sort() #오름차순 정렬
alpha.append(str(num_val)) #숫자 더한값 리스트에 삽입

result="".join(alpha) #문자열로 변환
print(result)