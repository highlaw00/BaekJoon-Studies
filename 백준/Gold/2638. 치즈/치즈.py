import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs_air():
    global grid
    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    q.append((0, 0))
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if not visited[ni][nj] and (grid[ni][nj] == 0 or grid[ni][nj] == 2):
                visited[ni][nj] = 1
                grid[ni][nj] = 2
                q.append((ni, nj))


grid[0][0] = 2
bfs_air()

cheeses = dict()
about_to_melt = dict()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            cnt = 0
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= n or nj >= m:
                    continue
                if grid[ni][nj] == 2:
                    cnt += 1
            info = (i, j)
            cheeses[info] = cnt
            if cnt >= 2:
                about_to_melt[info] = cnt


ans = 0
while len(cheeses):
    ans += 1
    for info in about_to_melt.keys():
        i, j = info
        grid[i][j] = 2
        del cheeses[info]
    about_to_melt = dict()
    bfs_air()
    for info in cheeses.keys():
        i, j = info
        cnt = 0
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if grid[ni][nj] == 2:
                cnt += 1
        cheeses[info] = cnt
        if cnt >= 2:
            about_to_melt[info] = cnt

print(ans)
