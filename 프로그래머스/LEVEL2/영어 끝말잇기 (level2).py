def solution(n,words):
  answer=[0,0]
  data=[]
  data.append(words[0]) # 첫단어 저장
  for i in range(1,len(words)):
    # 요구조건을 만족하면 리스트에 저장
    if words[i] not in data and words[i-1][-1] == words[i][0]:
      data.append(words[i])
    else:
      answer[0]=i%n+1
      answer[1]=i//n+1
      break
  return answer

solution(3,	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	)