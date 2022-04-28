def solution(s):
  result=[]
  head,number,tail="","",""
  for file in s:
    for i in range(len(file)):
      if file[i].isdigit(): # 숫자나오면 그 ㅇ전은 무조건 head, 그 이후는 number
        head=file[:i]
        number=file[i:]

        for j in range(len(number)): # number와 tail 구분
          if not number[j].isdigit():
            tail=number[j:]
            number=number[:j]
            break
        result.append([head,number,tail])
        head,number,tail="","",""
        break

  result.sort(key=lambda x:(x[0].upper(), int(x[1])))

  return ["".join(i) for i in result]           
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))