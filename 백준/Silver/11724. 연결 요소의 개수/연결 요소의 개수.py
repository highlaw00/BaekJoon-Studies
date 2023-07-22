import sys
sys.setrecursionlimit(1100)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 모든 노드에 대해서 DFS 진행


def dfs(v):
    # 현재 정점과 연결된 그래프를 가져와 순회합니다.
    nodes = graph[v]
    for node in nodes:
        if not visited[node]:
            visited[node] = 1
            dfs(node)


for i in range(1, n+1):
    # 방문 하지 않은 노드에 대해 DFS 진행
    if not visited[i]:
        cnt += 1
        visited[i] = 1
        dfs(i)

print(cnt)
