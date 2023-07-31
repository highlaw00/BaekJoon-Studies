import heapq
import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

n, m = map(int, input().rstrip().split())
# observable 값이 0이라면 통과 가능, 1이라면 통과 불가
observable = list(map(int, input().rstrip().split()))
graph = [[] for _ in range(n)]
dist = [INT_MAX for _ in range(n)]
dist[0] = 0

# 그래프 입력
for _ in range(m):
    a, b, t = map(int, input().rstrip().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

# Dijkstra init
# node 번호, node에 연결된 그래프, 거리를 우선순위 큐에 담습니다.
pq = []
heapq.heappush(pq, (0, 0))

# Dijkstra
while pq:
    # pq에 존재하는 node를 꺼내줍니다.
    node, min_dist = heapq.heappop(pq)
    if min_dist != dist[node]:
        continue

    # 현재 node에서 갈 수 있는 모든 노드의 dist를 갱신
    # 할 수 있으면 갱신합니다.
    for next_node in graph[node]:
        next, weight = next_node
        # 갈 수 있는 경우에만 dist를 확인합니다.
        # dist가 갱신되면 pq에 삽입합니다.
        if not observable[next] or next == n-1:
            alt = min_dist + weight
            if alt < dist[next]:
                dist[next] = alt
                heapq.heappush(pq, (next, alt))

if dist[n-1] == INT_MAX:
    print(-1)
else:
    print(dist[n-1])
