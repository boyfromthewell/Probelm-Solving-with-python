def solution(skill,skill_trees):
  answer=0
  for s in skill_trees:
    data=[]
    for j in s:
      if j in skill:
        data.append(j)

    # for-else문: for문이 break하지않고 끝가지 돌았다면 else문 실행
    for k in range(len(data)):
      if data[k]!=skill[k]:
        break
    else:
      answer+=1

  return answer