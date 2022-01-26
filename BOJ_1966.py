test_case=int(input())

for _ in range(test_case):
  n,m=map(int, input().split())
  s=list(map(int, input().split()))
  idx=[0 for _ in range(n)]

  idx[m]=1
  cnt=0
  while True:
    if s[0]==max(s):
      cnt+=1
      if idx[0]==1:
        print(cnt)
        break
      else:
        del s[0]
        del idx[0]
    else:
      s.append(s[0])
      del s[0]
      idx.append(idx[0])
      del idx[0] 

'''
중요도를 리스트에 담아준 다음 위치를 저장할 리스트도 만듬

차례로 검사하면서 제일 큰값이면 cnt에 1더하고 삭제

아니면 맨뒤에 넣어주고 삭제

만약 제일 큰값 찾고, 그 값이 내가 찾는 숫자이면 break
'''
