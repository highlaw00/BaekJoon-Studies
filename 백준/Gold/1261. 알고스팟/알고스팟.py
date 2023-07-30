import heapq as hq
import sys
input = sys.stdin.readline

INT_MAX = sys.maxsize
m, n = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[INT_MAX for _ in range(m)] for _ in range(n)]
dist[0][0] = 0
pq = []
ans = 0

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

# pq에 시작점 삽입 (dist, x, y)
hq.heappush(pq, (0, 0, 0))

# dijkstra 시작
while pq:
    min_dist, x, y = hq.heappop(pq)

    # 넣은 값이 현재와 다르다면 pass
    if min_dist != dist[x][y]:
        continue

    # 인접 방 탐색하며 갱신
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 인접 방까지의 거리 = 최소 비용 + 해당 방의 값
        alt = min_dist + maze[nx][ny]
        if dist[nx][ny] > alt:
            dist[nx][ny] = alt
            hq.heappush(pq, (alt, nx, ny))

print(dist[n-1][m-1])
