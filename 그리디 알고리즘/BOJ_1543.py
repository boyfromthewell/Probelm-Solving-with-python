import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

ans,i = 0,0

while i <= len(s)-len(p):
    if s[i:i+len(p)] == p:
        ans += 1
        i+=len(p)
    else:
        i+=1
print(ans)