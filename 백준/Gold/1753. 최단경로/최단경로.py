import heapq
import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

v, e = map(int, input().rstrip().split())
k = int(input().rstrip())
# 연결 그래프를 dict로 표현

graph = [dict() for _ in range(v+1)]
for _ in range(e):
    # u: 시작 노드, v: 끝 노드, w: 가중치
    s, e, w = map(int, input().rstrip().split())
    d = graph[s]
    # 이미 존재한다면 최소값 갱신
    if e in d:
        d[e] = min(d[e], w)
    else:
        d[e] = w

# k번 노드부터 dijkstra 시작
# dijkstra: 우선순위 큐를 활용해 현재 방문하지 않았으며
# 비용이 최소인 노드를 방문하며 남아있는 노드의 비용을 갱신하는 방식
visited = [0 for _ in range(v+1)]
dist = [INT_MAX for _ in range(v+1)]
pq = []

# push: node_idx & distance
# 오답노트: distance를 기준으로 정렬해야함
heapq.heappush(pq, (0, k))
visited[k] = 1
dist[k] = 0

while pq:
    min_dist, curr = heapq.heappop(pq)

    # 우선순위 큐에 삽입된 거리값과 현재 갱신된 거리값이 다른 경우
    # 이 경우 continue하지 않아도 상관없지만 최적화를 위해 진행
    if min_dist != dist[curr]:
        continue

    for node, distance in graph[curr].items():
        alt = min_dist + distance
        # 최소 비용 갱신
        if dist[node] > alt:
            dist[node] = alt
            # 우선순위 큐에 삽입함으로써, 방문했음을 알 수 있음
            # 최소거리가 갱신된 노드에 대해서만 주변 노드를 탐색해야함
            heapq.heappush(pq, (alt, node))

for i in range(1, v+1):
    if dist[i] == INT_MAX:
        print('INF')
    else:
        print(dist[i])
