import sys
input=sys.stdin.readline

def find_parent(parent,x):
  # 루트 노드가 아니라면, 루트노드를 찾을 때 까지 재귀적으로 호출
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n,m=map(int,input().split())
parent=[0]*(n+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result=0
# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, n+1):
  parent[i]=i

for _ in range(m):
  a,b,c=map(int,input().split())
  # 비용순으로 정렬하기 위해 튜플의 첫번쨰 원소를 비용으로 설정
  edges.append((c,a,b))

# 간선을 비용순으로 정렬
edges.sort()
last=0 # 최소 신장트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:
  cost,a,b=edge
  # 사이클이 발생하지 않는 경우 집합에 포함
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost
    last=cost  # 비용순으로 정렬 되어있기 때문에 가장 마지막에는 최소 신장트리 중에 가장 큰 간선값이 last 에 담길것

print(result-last)