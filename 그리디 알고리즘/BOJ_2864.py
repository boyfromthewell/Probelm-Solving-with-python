a,b=input().split()

# replace 함수:어떤 값 바꿔줌 -> a.replace('6', '5') -> a의 문자열에서 6을 5로 바꾸겠다!!!!!!!!
min_val=int(a.replace('6', '5'))+int(b.replace('6','5'))
max_val=int(a.replace('5', '6'))+int(b.replace('5','6'))

print(min_val, max_val)