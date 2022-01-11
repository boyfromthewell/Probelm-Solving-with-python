n=int(input())

data=[]
for _ in range(n):
  word=str(input())
  word_cnt=len(word)
  data.append((word, word_cnt))

#중복 삭제
data=list(set(data))

# 단어 길이 먼저 정렬하기
data.sort(key=lambda x: (x[1], x[0]))
for i in data:
  print(i[0])