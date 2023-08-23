# 1 ~ N 정점에서 X 정점까지의 거리를 구하는 방법
# 일반적으로 구하면, 1 ~ N 모든 정점을 시작 정점으로 두고 다익스트라를 진행
# => O(V^3) or O(VElogV)

# X 정점에서 1~N 정점까지의 최단 거리는 다익스트라 한 번으로 구할 수 있음
# 왜? X에서 1~N까지의 모든 경우의 거리를 구하기 때문

# 1 ~ N 정점부터 X 정점까지의 거리는 어떻게 빨리 구할 수 있을까?
# 만약 1 ~ N의 모든 정점이 X와 연결이 되어있음이 보장된다면,
# 모든 간선의 방향을 바꾸고 X에서 모든 정점에 대한 최단 거리를 구하면 다익스트라 한 번에 구할 수 있다.

import sys
import heapq
input = sys.stdin.readline
INT_MAX = sys.maxsize

n, m, x = map(int, input().rstrip().split())
# graphs: 원래 방향의 그래프
# inverse_graphs: 간선의 방향이 바뀐 그래프, 1~N 정점 부터 X 정점까지의 거리를 담음
graphs = [[] for _ in range(n+1)]
inverse_graphs = [[] for _ in range(n+1)]
dists = [INT_MAX for _ in range(n+1)]
inverse_dists = [INT_MAX for _ in range(n+1)]

# 그래프 입력
# 시작점, 끝점, 비용 주어짐
for _ in range(m):
    s, e, c = map(int, input().rstrip().split())
    graphs[s].append((e, c))
    inverse_graphs[e].append((s, c))

# 원래의 그래프에서 X를 시작 정점으로 하는 다익스트라 => 돌아가는 비용
# 역순의 그래프에서 X를 시작 정점으로 하는 다익스트라 => X로 오는 비용


def dijkstra(start, dists, graphs):
    dists[start] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, start))
    while min_heap:
        curr_cost, curr_node = heapq.heappop(min_heap)
        if curr_cost != dists[curr_node]:
            continue
        # 연결된 모든 정점 확인 및 갱신
        for next_node, val in graphs[curr_node]:
            if curr_cost + val < dists[next_node]:
                dists[next_node] = curr_cost + val
                heapq.heappush(min_heap, (dists[next_node], next_node))


dijkstra(x, dists, graphs)
dijkstra(x, inverse_dists, inverse_graphs)


ans = dists[1] + inverse_dists[1]
for i in range(1, n+1):
    candidate = dists[i] + inverse_dists[i]
    ans = max(ans, candidate)

print(ans)
