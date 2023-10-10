import sys
from collections import deque
n, k = map(int, input().split())


# bfs 진행
# 거리 배열 필요
# visited[i] = i번째 좌표까지의 최소 비용으로 도달할 수 있는 방법 개수
visited = [0 for _ in range(100_001)]
# dists[i] = i번째 좌표까지의 최소 비용
dists = [0 for _ in range(100_001)]
target_dist = 0
cnt = 1  # 어떻게든 최소 1개의 경로는 존재.
q = deque()
q.append((n, 0))
visited[n] = 1

while q:
    x, dist = q.popleft()
    # x - 1, x + 1, x * 2
    for dx in (1, -1, x):
        nx = x + dx
        if nx < 0 or nx >= len(visited):
            continue
        # 첫 방문인 경우
        if not visited[nx]:
            visited[nx] += 1
            dists[nx] = dist + 1
            q.append((nx, dist+1))
        # 이전에 방문했으나 새로운 방법을 찾은 경우
        elif dists[nx] == dist + 1:
            visited[nx] += 1
            q.append((nx, dist+1))

print(dists[k])
print(visited[k])
