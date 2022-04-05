def find_parent(parent,x):
  # 루트 노드가 아니라면 루트노드를 찾을때까지 재귀적으로 호출
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

g=int(input())
p=int(input())
parent=[0]*(g+1)

for i in range(1,g+1):
  parent[i]=i

result=0
for _ in range(p):
  data=find_parent(parent,int(input()))
  if data==0: # 현재 루트가 0이면 종료
    break
  union_parent(parent,data,data-1) # 그렇지 않으면 바로 왼쪽의 집합과 합치기
  result+=1

print(result)

  