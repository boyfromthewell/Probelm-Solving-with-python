def solution(dirs):
  answer=0
  result=set()
  data={"U":[0,1], "D":[0,-1], "R":[1,0], "L":[-1,0]}

  x,y=0,0
  
  for i in dirs:
    nx=x+data[i][0]
    ny=y+data[i][1]
    if -5<=nx<=5 and -5<=ny<=5:
      m1=(x,y,nx,ny)
      m2=(nx,ny,x,y)
      if m1 not in result:
        result.add(m1)
        result.add(m2)
        answer+=1
      x,y=nx,ny
      
  return answer

print(solution("ULURRDLLU"))
  