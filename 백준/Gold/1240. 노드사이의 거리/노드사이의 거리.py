import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# 트리 구조가 입력됩니다.
edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().rstrip().split())
    edges[u].append((v, w))
    edges[v].append((u, w))


def dfs(u, w_sofar, target):
    global visited, dist
    for child, weight in edges[u]:
        if not visited[child]:
            visited[child] = True
            if child == target:
                dist = w_sofar + weight
                return
            dfs(child, w_sofar + weight, target)

    # 정점 u부터 정점 v까지의 거리를 묻는 쿼리가 m개 주어집니다.
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    # 트리 구조이기 때문에 dfs를 통해 정점간의 거리를 구할 수 있습니다.
    visited = [False for _ in range(n+1)]
    visited[a] = True
    dist = -1
    dfs(a, 0, b)
    print(dist)
