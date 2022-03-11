def solution(skill, skill_trees):
  answer=0
  for i in skill_trees:
    list=[]
    for j in i:
      if j in skill:
        list.append(j)
    print(list)
    # for-else문: for문이 중간에 break로       중단되지 않고, 끝까지 시행되었을때 작동하      게 됨
    for k in range(len(list)):
      if list[k]!=skill[k]:
        break
    else:
      answer+=1

  return answer
  
print(solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]))