# 픽셀 정보를 받고, 정상인 경우 구역이 몇 개 나오는지 부터 구해봅시다.
# 정상 => R,G,B 가 모두 다른 구역
# 색약 => R,G 가 같은 구역, B가 다른 구역
from collections import deque

n = int(input())

pixels = [input() for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
visited_disabled = [[0 for _ in range(n)] for _ in range(n)]
q = deque()
normal_cnt = 0
disabled_cnt = 0
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs():
    global q, pixels, visited
    while q:
        i, j, val = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue
            if pixels[ni][nj] == val and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj, pixels[ni][nj]))


def bfs_disabled():
    global q, pixels, visited
    while q:
        i, j, val = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue
            if not visited_disabled[ni][nj]:
                if val == 'B' and pixels[ni][nj] == val:
                    visited_disabled[ni][nj] = 1
                    q.append((ni, nj, pixels[ni][nj]))
                elif val in ('R', 'G') and pixels[ni][nj] in ('R', 'G'):
                    visited_disabled[ni][nj] = 1
                    q.append((ni, nj, pixels[ni][nj]))


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            normal_cnt += 1
            visited[i][j] = 1
            q.append((i, j, pixels[i][j]))
            bfs()
        if not visited_disabled[i][j]:
            disabled_cnt += 1
            visited_disabled[i][j] = 1
            q.append((i, j, pixels[i][j]))
            bfs_disabled()

print(normal_cnt, disabled_cnt)
