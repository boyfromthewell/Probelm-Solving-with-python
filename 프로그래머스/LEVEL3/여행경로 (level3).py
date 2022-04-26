from collections import defaultdict

def solution(tickets):
  dic=defaultdict(list)
  for ticket in tickets:
    dic[ticket[0]].append(ticket[1])

  # 딕셔너리 value들 역순으로 정렬
  for i in dic.keys():
    dic[i].sort(reverse=True)

  stack=["ICN"]
  result=[]

  while stack:
    top=stack[-1]
    # 경로가 없으면 result 배열에 넣어주기
    if not dic[top]:
      result.append(stack.pop())
    # 경로가 존재하면 스택에 쌓아주기
    else:
      stack.append(dic[top].pop())
  return result[::-1]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))