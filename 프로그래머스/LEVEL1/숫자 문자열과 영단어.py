def solution(s):
  
  dic={'zero':0, "one":1, "two":2, "three":3, "four":4, "five":5,"six":6,"seven":7,"eight":8,"nine":9}

  answer=""
  temp=""
  
  for i in s:
    # 숫자로 시작하면 그냥 이어 붙이기
    if i.isdigit():
      answer=answer+i
    # 문자열로 시작하면 임시 변수에 붙이고
    elif i.isalpha():
      temp=temp+i
      # 딕셔너리 키에 temp 문자열과 일치하는 값이 있다면
      if temp in dic.keys():
        # 딕셔너리 value값 이어 붙이기
        answer=answer+str(dic[temp])
        temp=''

  return int(answer)


print(solution("one4seveneight"))