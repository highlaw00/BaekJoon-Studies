import sys
import heapq as hq
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start, graph):
    dists = [INF for _ in range(len(graph))]
    pq = []
    dists[start] = 0
    # dist, node_number 를 힙에 삽입
    hq.heappush(pq, (0, start))
    
    while pq:
        dist, node = hq.heappop(pq)
        if dist > dists[node]:
            continue
        for next_node, weight in graph[node]:
            alt_weight = dist + weight
            if alt_weight >= dists[next_node]:
                continue
            dists[next_node] = alt_weight
            hq.heappush(pq, (alt_weight, next_node))
    
    return dists

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    # 의존성 그래프
    dependencies = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        # b -> a 의 경로가 s 가중치를 가진다.
        dependencies[b].append((a, s))
    
    # 해킹당한 컴퓨터로부터 다익스트라 시작
    dist_arr = dijkstra(c, dependencies)
    hacked_computer = 0
    hacked_time = 0
    for dist in dist_arr:
        if dist != INF:
            hacked_computer += 1
            hacked_time = max(hacked_time, dist)
    
    print(hacked_computer, hacked_time)