def sol(s):
  ans=len(s)
  # 1개 단위(step)부터 압축 단위를 늘려가며 확인
  for step in range(1, len(s)//2+1):
    compressed=""
    prev=s[0:step] #앞에서 step만큼 문자열 추출
    count=1
    # step 만틈 증가시키며 이전 문자열과 비고
    for j in range(step,len(s), step):
      #이전 상태와 동일 하다면 압축횟수(cnt)증가
      if prev==s[j:j+step]:
        count+=1
      #다른 문자열이 나왔다면
      else:
        compressed+=str(count)+prev if count>=2 else prev
        prev=s[j:j+step] #다시 상태 초기화
        count=1
    #남아있는 문자열 처리
    compressed+=str(count)+prev if count>=2 else prev
    #만들어진 압축 문자열이 가장 짧은것이 정답
    ans=min(ans, len(compressed))
    print(compressed)
  return ans

result=sol("aaaabbabbabb")
print(result)
