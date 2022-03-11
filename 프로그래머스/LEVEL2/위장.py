def solution(clothes):
  dic={}
  answer=1

  #현재 옷종류가 dic에 있으면 append로 값추가, 없으면 리    스트로 추가
  for cloth in clothes:
    if cloth[1] in dic.keys():
      dic[cloth[1]].append(cloth[0]) 
    else:
      dic[cloth[1]]=[cloth[0]]

  for i in dic.values():
    answer*=len(i)+1

  return answer-1 # 아무것도 안입는 경우 1을 빼기
