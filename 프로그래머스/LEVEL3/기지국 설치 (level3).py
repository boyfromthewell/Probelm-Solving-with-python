import math

def solution(n, stations, w):
  answer = 0
  distance=[]

  # 설치된 기지국사이에 전파가 닿지 않는 거리 저장
  for i in range(1, len(stations)):
    distance.append((stations[i]-w-1)-(stations[i-1]+w))

  # 맨 앞 기지국에서 첫번째 아파트 사이에 전파 닿지않는거리,
  # 맨 뒤 기지국에서 마지막 아파트 사이에 전파 닿지 않는 거리 저장
  distance.append(stations[0]-w-1)
  distance.append(n-(stations[-1]+w))

  for i in distance:
    # 닿지 않는 거리가 0이하일 경우 continue
    if i<=0:
      continue
    # 닿지 않는 거리에 설치 할 수 있는 최소 개수 더하기
    answer+=math.ceil(i/((w*2)+1))

  return answer

print(solution(11,	[4, 11],	1))