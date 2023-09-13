from collections import deque

n = int(input())
grid = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
house_cnt = []


def bfs(i, j):
    global cnt, visited
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        cnt += 1
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue
            if grid[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))


for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            cnt = 0
            bfs(i, j)
            house_cnt.append(cnt)

house_cnt.sort()
print(len(house_cnt))
for cnt in house_cnt:
    print(cnt)
