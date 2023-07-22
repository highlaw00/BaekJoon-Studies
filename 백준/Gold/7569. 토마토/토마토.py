import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
grid = [[list(map(int, input().split())) for _ in range(n)]
        for _ in range(h)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque()
sub_q = deque()
# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dirs = [(-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0)]
day = 0

# 익은 토마토 조사
immatures = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            tomato = grid[i][j][k]
            if tomato == 1:
                q.append((i, j, k))
            elif tomato == 0:
                immatures += 1

if not immatures:
    print(0)
    exit()

visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
# 익은 토마토로 BFS 진행
while True:
    while q:
        i, j, k = q.popleft()
        visited[i][j][k] = 1
        for di, dj, dk in dirs:
            ni, nj, nk = i + di, j + dj, k + dk
            if ni < 0 or nj < 0 or nk < 0 or ni >= h or nj >= n or nk >= m:
                continue
            if grid[ni][nj][nk] == 0 and not visited[ni][nj][nk]:
                immatures -= 1
                visited[ni][nj][nk] = 1
                sub_q.append((ni, nj, nk))

    if not len(sub_q):
        break

    # sub_q의 내용을 q에 push
    while sub_q:
        i, j, k = sub_q.popleft()
        grid[i][j][k] = 1
        q.append((i, j, k))

    day += 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if visited[i][j][k] == 0 and grid[i][j][k] != -1:
                print(-1)
                exit()

# 익은 경우 익는데 걸린 최소 일수 출력
print(day)
