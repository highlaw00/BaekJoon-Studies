
# 1. 간선 오름차순 정렬
# 2. 현재 간선을 추가했을 때 사이클이 발생하는지 확인
# 3. 사이클이 발생한다면 해당 간선 스킵
# 4. 사이클이 발생하지 않는다면 해당 간선을 추가
# 5. 선택한 간선이 v-1개가 될 때까지 2~4 과정을 반복
# 6. 가중치 총합해서 출력

import sys
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    edges.append((a, b, c))

# 간선 오름차순 정렬
edges.sort(key=lambda x: [x[2]])
mst = []
uf = [i for i in range(v + 1)]


def union(x, y):
    # 합집합
    X = find(x)
    Y = find(y)
    uf[X] = Y


def find(x):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]


for edge in edges:
    if len(mst) >= v - 1:
        break
    # 현재 간선을 추가했을 때 사이클이 생기는지 확인
    # 현재 간선의 끝 정점들이 같은 집합에 포함해있으면 사이클 발생
    a, b, c = edge
    if find(a) == find(b):
        continue
    union(a, b)
    mst.append(c)

print(sum(mst))
