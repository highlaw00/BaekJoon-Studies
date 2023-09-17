n = int(input())
m = int(input())

# union find
# union - 다른 두 원소가 존재하는 집합을 하나의 집합으로 합치는 연산
# find - 원소가 속한 집합의 대표값을 찾는 연산

# i도시와 j도시가 연결됨 -> union 연산
# i도시와 j도시가 연결되지 않음 -> 무시

uf = [i for i in range(n+1)]

# union 연산은 x의 루트 원소를 y의 루트 원소로 바꿔주는 연산


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    uf[x_root] = y_root

# find 연산은 x의 루트 원소를 찾는 연산


def find(x):
    # 주어진 원소가 루트 원소라면 return
    if x == uf[x]:
        return x
    # 아니라면 현재 부모 노드의 루트 노드를 찾는다.
    root_node = find(uf[x])
    uf[x] = root_node
    return root_node


for i in range(1, n+1):
    line = [0] + list(map(int, input().split()))
    for j in range(1, n+1):
        if line[j] == 1:
            union(i, j)

planned_cities = list(map(int, input().split()))
# 처음으로 방문할 도시의 루트 원소를 찾아둡니다. (비교를 위해)
criterion_val = find(planned_cities[0])
flag = True
for city in planned_cities:
    root_val = find(city)
    if criterion_val != root_val:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
