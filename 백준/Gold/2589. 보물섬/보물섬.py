import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
q = deque()
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs():
    global q
    ret = -1
    while q:
        ret += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= n or nj >= m:
                    continue
                if not visited[ni][nj] and grid[ni][nj] == 'L':
                    visited[ni][nj] = 1
                    q.append((ni, nj))
    return ret


# 모든 L에 대해서 BFS를 진행
ans = 0
for i in range(n):
    for j in range(m):
        status = grid[i][j]
        if status == 'L':
            visited = [[0 for _ in range(m)] for _ in range(n)]
            visited[i][j] = 1
            q.append((i, j))
            ans = max(ans, bfs())

print(ans)
