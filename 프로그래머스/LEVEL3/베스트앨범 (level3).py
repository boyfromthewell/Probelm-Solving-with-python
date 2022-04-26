def solution(genres, plays):
  answer=[]
  dic={}
  # dic에 {장르1: [[노래1 재생횟수, 인덱스], [노래2 재생횟수, 인덱스]]...} 형식으로 저장
  for i in range(len(genres)):
    if genres[i] in dic:
      dic[genres[i]].append([plays[i],i])
    else:
      dic[genres[i]]=[[plays[i],i]]   # dic2에 각장르 모든곡의 총재생 횟수 저장 {장르1: 장르1의 총 재생횟수,,,, }
  dic2={}
  for genre in dic.keys():
    songs=dic[genre]
    plays_sum=0
    for song in songs:
      plays_sum+=song[0]
    dic2[genre]=plays_sum
    
  # dic2를 총재생횟수 내림차순 순으로 정렬
  dic2=sorted(dic2.items(), key=lambda x:x[1], reverse=True) 
  
  # dic2에 저장된 장르 순으로 dic에서 해당 장르 key로 가진 value 확인
  for genre in dic2:
    # 2차원 배열인 value를 다중 조건으로 정렬 (첫번째 인자의 곡 재생수 기준 내림차순, 두번째 인자인 곡 고유번호 기준 오름차순)
    song_rank=sorted(dic[genre[0]], key=lambda x:(-x[0],x[1]))
    cnt=0
    # 정렬된 배열 하나씩 확인하면서 answer에 고유 번호 순서대로 저장, 한장르에 두곡 저장되면 break
    for song in song_rank:
      answer.append(song[1])
      cnt+=1
      if cnt==2:
        break

  return answer
  
print(solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]))