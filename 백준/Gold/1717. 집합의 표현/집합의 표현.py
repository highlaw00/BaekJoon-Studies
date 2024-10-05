import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

n, m = map(int, input().split())
# 집합 표현
sets = [i for i in range(n+1)]

# union - find
def union(a, b):
  a_parent = find(a)
  b_parent = find(b)
  if (a_parent != b_parent):
    # 부모 노드의 union이 필요
    sets[a_parent] = b_parent

def find(a):
  # 부모 노드와 본인이 동일할 때
  if a == sets[a]:
    return a
  # 부모 노드가 본인과 다를 때
  ancestor = find(sets[a])
  sets[a] = ancestor
  return ancestor

for _ in range(m):
  x, v1, v2 = map(int, input().split())
  if x:
    v1_p = find(v1)
    v2_p = find(v2)
    if v1_p == v2_p:
      print('YES')
    else:
      print('NO')
  else:
    union(v1, v2)