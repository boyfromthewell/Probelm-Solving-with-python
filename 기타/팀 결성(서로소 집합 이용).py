def find_parent(parent,x):
  # 루트 노드가 아니라면 루트 노드를 찾을때까지 재귀 호출
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

# 두원소 속한 집합 합치기
def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n,m=map(int,input().split())
parent=[0]*(n+1) # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(0,n+1):
  parent[i]=i

# 각 연산을 하나씩 확인
for _ in range(m):
  oper,a,b=map(int,input().split())
  # 합집합 연산일 경우
  if oper==0:
    union_parent(parent,a,b)
  elif oper==1:
    if find_parent(parent,a)==find_parent(parent,b):
      print("YES")
    else:
      print("NO")