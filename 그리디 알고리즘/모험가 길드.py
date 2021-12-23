#이코테 311p
n=int(input())
data=list(map(int, input().split()))
data.sort()

result=0 #총 그룹의 수
count=0 #현재 그룹에 포함된 모험가수

for i in data: #공포도 낮은거 부터 확인
  count+=1 #현재그룹에 해당 모험가 포함
  if count>=i: #현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이면 그룹 결성
    result+=1 #총 그룹수 증가
    count=0 #모험가 수 초기화
print(result)