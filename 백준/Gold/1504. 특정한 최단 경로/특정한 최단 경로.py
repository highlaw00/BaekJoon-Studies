import sys
import heapq
INT_MAX = sys.maxsize

input = sys.stdin.readline
n, e = map(int, input().rstrip().split())
graphs = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    graphs[a].append([b, c])
    graphs[b].append([a, c])

v1, v2 = map(int, input().rstrip().split())


def dijkstra(start, target):
    dists = [INT_MAX for _ in range(n+1)]
    dists[start] = 0

    # 1번부터 Dijkstra 시작
    min_heap = []
    # Min Heap에는 (dist, node number) 삽입
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        curr_dist, curr_node = heapq.heappop(min_heap)
        # 삽입 된 이후 거리가 갱신되었다면 넘어갑니다
        if curr_dist != dists[curr_node]:
            continue
        # 인접한 노드의 거리를 갱신합니다
        for vertex, val in graphs[curr_node]:
            # 현재 노드를 통해 인접 노드로 방문하는 비용이 더 작은 경우에 갱신
            # 갱신되었다면 큐에 삽입
            if curr_dist + val < dists[vertex]:
                dists[vertex] = curr_dist + val
                heapq.heappush(min_heap, (dists[vertex], vertex))

    if dists[target] == INT_MAX:
        return -1
    else:
        return dists[target]


# v1 -> v2로 가는 경우
v1_v2 = dijkstra(v1, v2)
one_v1 = dijkstra(1, v1)
v2_n = dijkstra(v2, n)


# v2 -> v1로 가는 경우
one_v2 = dijkstra(1, v2)
v1_n = dijkstra(v1, n)

ans1 = 0
ans2 = 0
for cost in [one_v1, v1_v2, v2_n]:
    if cost == -1:
        ans1 = INT_MAX
        break
    else:
        ans1 += cost

for cost in [one_v2, v1_v2, v1_n]:
    if cost == -1:
        ans2 = INT_MAX
        break
    else:
        ans2 += cost

ans = min(ans1, ans2)
if ans == INT_MAX:
    print(-1)
else:
    print(ans)
