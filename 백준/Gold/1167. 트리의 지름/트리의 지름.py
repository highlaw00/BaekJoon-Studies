import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

v = int(input())
edges = [[] for _ in range(v+1)]

for _ in range(v):
    line = list(map(int, input().rstrip().split()))
    s, e, w = 0, 0, 0
    for i, val in enumerate(line):
        if val == -1:
            break
        if i == 0:
            s = val
        elif i % 2 == 1:
            e = val
        else:
            w = val
            edges[s].append((e, w))


def dfs(parent, prev_weight, dists, visited):
    for child, weight in edges[parent]:
        if not visited[child]:
            dists[child] = prev_weight + weight
            visited[child] = True
            dfs(child, dists[child], dists, visited)

# 1번 정점부터 DFS를 진행하여, 1번 정점에서 제일 먼 정점을 구합니다.


def get_radius(start_v):
    # 거리 배열 선언
    dists = [-1 for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    dists[start_v] = 0
    visited[start_v] = True
    dfs(start_v, 0, dists, visited)

    second_start_v = -1
    max_dist = -1
    for i in range(1, v+1):
        if dists[i] > max_dist:
            second_start_v = i
            max_dist = dists[i]

    dists = [-1 for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    dists[second_start_v] = 0
    visited[second_start_v] = True
    dfs(second_start_v, 0, dists, visited)

    return max(dists)


ans = get_radius(1)
print(ans)
