import sys
sys.setrecursionlimit(100_001)
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().rstrip().split())
    edges[s].append(e)
    edges[e].append(s)

visited = [False for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

visited[1] = True
# 1번부터 dfs를 진행합니다.


def dfs(parent):
    for v in edges[parent]:
        if not visited[v]:
            visited[v] = True
            parents[v] = parent
            dfs(v)


dfs(1)
for i in range(2, n+1):
    print(parents[i])
