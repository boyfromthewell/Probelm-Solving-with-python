import itertools

data=[1,2,3]

print("순열")
# 순열 (서로 다른 n개에서 r개 선택 일렬로 나열)
for x in itertools.permutations(data,2):
  print(list(x), end=" ")
print()
# 조합 (서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택 하는것)
print("조합")
for x in itertools.combinations(data,2):
  print(list(x), end=" ")
