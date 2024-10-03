import sys
import heapq as hq
INF = sys.maxsize

v, e = map(int, input().split())
graphs = [[] for _ in range(v+1)]
k = int(input())

for _ in range(e):
    s, d, w = map(int, input().split())
    graphs[s].append((d, w))

# dijkstra 실행
dists = [INF for _ in range(v+1)]
heap = [(0, k)] # k번째 노드부터 시작. (dist, node_num)
dists[k] = 0

while heap:
    curr_dist, curr_node = hq.heappop(heap)
    if dists[curr_node] < curr_dist:
        continue
    for next_node, weight in graphs[curr_node]:
        alt_dist = curr_dist + weight
        if alt_dist < dists[next_node]:
            dists[next_node] = alt_dist
            hq.heappush(heap, (dists[next_node], next_node))

for i in range(1, v+1):
    dist = dists[i]
    if dist == INF:
        print('INF')
    else:
        print(dist)