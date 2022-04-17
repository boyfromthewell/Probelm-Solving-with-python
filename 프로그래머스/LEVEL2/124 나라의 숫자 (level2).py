def solution(n):
    array=[1,2,4]
    answer=""
    while n>0:
        n-=1
        answer=str(array[n%3])+answer
        n//=3
        
    return answer

print(solution(9))