import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())
graphs = [dict() for _ in range(n+1)]
for _ in range(m):
    s, d, w = map(int, input().split())
    if s == d:
        continue
    if d not in graphs[s]:
        graphs[s][d] = w
    else:
        min_weight = min(graphs[s][d], w)
        graphs[s][d] = min_weight

start_node, dest_node = map(int, input().split())

pq = []
dists = [INF for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
heapq.heappush(pq, (0, start_node))
dists[start_node] = 0

while pq:
    curr_dist, curr_node = heapq.heappop(pq)
    if curr_dist > dists[curr_node]:
        continue
    
    for next_node, weight in graphs[curr_node].items():
        alt_dist = curr_dist + weight
        if alt_dist >= dists[next_node]:
            continue
        if parent[curr_node] == next_node:
            continue
        dists[next_node] = alt_dist
        parent[next_node] = curr_node
        heapq.heappush(pq, (alt_dist, next_node))

path = [dest_node]
curr_node = dest_node
while parent[curr_node] != -1:
    path.append(parent[curr_node])
    curr_node = parent[curr_node]

print(dists[dest_node])
print(len(path))
print(' '.join(map(str, reversed(path))))