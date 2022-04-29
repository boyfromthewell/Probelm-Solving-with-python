def solution(s):
  cnt1=0 # 0 개수 담을 변수
  cnt2=0 # 변환 횟수 담을 변수
  while True:
    cnt2+=1
    cnt1+=s.count("0") # 0 개수 새기
    s=s.replace("0","") # 0 제거
    next_s=bin(len(s))[2:] # s를 2진법으로 바꾸기
    if next_s=="1":
      break
    else:
      s=next_s

  return [cnt2,cnt1]
    