import sys
sys.setrecursionlimit(100_002)
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().rstrip().split())
    edges[p].append((c, w))
    edges[c].append((p, w))


def dfs(parent, base_dist, visited, dists):
    for child, weight in edges[parent]:
        if not visited[child]:
            visited[child] = True
            dists[child] = base_dist + weight
            dfs(child, dists[child], visited, dists)


def get_radius(start_v):
    # start_v에서 dfs를 진행하고 가장 멀리 존재하는 노드에서 다시 DFS를 진행합니다.
    visited = [False for _ in range(n+1)]
    dists = [-1 for _ in range(n+1)]
    visited[start_v] = True
    dists[start_v] = 0
    dfs(start_v, dists[start_v], visited, dists)

    # 1번 노드에서 가장 먼 노드를 찾습니다.
    farthest_v = -1
    max_dist = 0
    for i in range(1, n+1):
        if dists[i] > max_dist:
            farthest_v = i
            max_dist = dists[i]

    # 1번 노드에서 가장 먼 노드에서 dfs를 진행합니다
    start_v = farthest_v
    visited = [False for _ in range(n+1)]
    dists = [-1 for _ in range(n+1)]
    visited[start_v] = True
    dists[start_v] = 0
    dfs(start_v, dists[start_v], visited, dists)

    return max(dists)


ans = get_radius(1)
print(ans)
