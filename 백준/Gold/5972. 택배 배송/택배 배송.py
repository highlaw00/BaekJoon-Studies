import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())
graphs = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graphs[a].append((b, c))
    graphs[b].append((a, c))
    
dists = [INF for _ in range(n+1)]
pq = []
dists[1] = 0
# 우선순위 큐 (dist, node_num) 삽입
heapq.heappush(pq, (0, 1))

while pq:
    curr_dist, curr_node = heapq.heappop(pq)
    if dists[curr_node] < curr_dist:
        continue
    
    for next_node, weight in graphs[curr_node]:
        alt_dist = curr_dist + weight
        if alt_dist >= dists[next_node]:
            continue
        dists[next_node] = alt_dist
        heapq.heappush(pq, (alt_dist, next_node))

print(dists[n])