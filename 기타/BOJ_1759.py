from itertools import combinations

vowels=['a','e','i','o','u'] # 5개 모음 정의
l,c=map(int,input().split())
# 가능한 암호 사전식으로 출력해야 함으로 입력이후 정렬
data=input().split()
data.sort()

# 길이가 l인 모든 암호조합 확인
for pwd in combinations(data,l):
  모음cnt=0
  자음cnt=0
  for i in pwd:
    if i in vowels:
      모음cnt+=1
    else:
      자음cnt+=1
  # 최소 1개의 모음과 최소 2개의 자음이 있으면 출력
  if 모음cnt>=1 and 자음cnt>=2:
    print("".join(pwd))
  
