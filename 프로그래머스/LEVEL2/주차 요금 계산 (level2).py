import math

def time_to_minutes(time):
  h,m=map(int,time.split(":"))
  return h*60+m

def solutions(fees,records):
  result=[]
  기본시간,기본요금,단위시간,단위요금=fees
  dic=dict()
  for r in records:
    # 차량번호 별로 주차시간과, inorout 저장
    시간,차량번호,INorOUT=r.split()
    차량번호=int(차량번호)

    if 차량번호 in dic:
      dic[차량번호].append([time_to_minutes(시간),INorOUT])
    else:
      dic[차량번호]=[[time_to_minutes(시간),INorOUT]]

  #print(dic)
  # 차량번호를 기준으로 딕셔너리를 오름차순 정렬
  data_list=sorted(dic.items())

  #print(data_list)

  for i in data_list:
    time=0
    for j in i[1]: 
      if j[1]=="IN": # inorout이 in이면
        time-=j[0] # 시간 빼기
      elif j[1]=="OUT": # out 이면
        time+=j[0] # 시간 더하기

    if i[1][-1][1]=="IN": # 마지막에 출차내역이 없는경우
      time+=time_to_minutes("23:59") # 출차시간 23:59로 넣기

    if time<=기본시간: # 기본시간보다 적으면 기본요금 추가
      result.append(기본요금)
    else: # 기본시간 이상 이면
      result.append(기본요금+math.ceil((time-기본시간)/단위시간)*단위요금)

  return result

    


#print(solutions([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))   
    
  
  