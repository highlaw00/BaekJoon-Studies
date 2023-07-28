import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

n = int(input())
m = int(input())
graph = [[-1 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n)]
dist = [INT_MAX for _ in range(n)]

# 그래프 입력
for _ in range(m):
    s, e, v = map(int, input().rstrip().split())
    s, e = s - 1, e - 1
    if graph[s][e] == -1:
        graph[s][e] = v
    else:
        graph[s][e] = min(v, graph[s][e])

# 시작 도시, 도착 도시
s, e = map(int, input().rstrip().split())
dist[s-1] = 0

# 모든 정점에 대해 조사
for _ in range(n):
    # 방문하지 않았으며 현재 최단 거리인 도시
    min_val = INT_MAX
    min_idx = 0

    for i in range(n):
        if not visited[i] and min_val >= dist[i]:
            min_val = dist[i]
            min_idx = i

    visited[min_idx] = 1

    # 현재 정점과 연결된 모든 노드 확인
    # 연결된 노드의 거리를 필요시 갱신
    for i in range(n):
        # 연결되지 않은 경우 무시
        if graph[min_idx][i] == -1:
            continue
        dist[i] = min(dist[i], dist[min_idx] + graph[min_idx][i])

print(dist[e-1])
