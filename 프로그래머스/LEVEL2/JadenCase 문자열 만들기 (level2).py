def solution(s):
  answer=""
  data=s.split(" ")
  for i in range(len(data)):
    # capitalize() : 문자열 첫번째 글자만 대문자로 변환
    data[i]=data[i].capitalize()

  answer=" ".join(data)
  return answer

print(solution("adf df dfd"))