import sys
from collections import deque
input = sys.stdin.readline
# BFS 를 단계적으로 진행
# 만약 BFS를 다 돌았는데 익지않은 토마토가 존재한다면 -1
# 처음부터 안 익은 토마토가 하나도 없다면 0

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
sub_q = deque()
day = 0
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    for j in range(m):
        tomato = grid[i][j]
        if tomato == 1:
            q.append((i, j))
            visited[i][j] = 1

while True:
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            # 인접한 토마토가 익지 않았다면 sub_q에 append
            if grid[ni][nj] == 0 and not visited[ni][nj]:
                sub_q.append((ni, nj))
                visited[ni][nj] = 1
                grid[ni][nj] = 1

    # sub_q가 비어있다면 익을 수 있는 토마토가 모두 익었다는 의미
    if not len(sub_q):
        break

    # sub_q를 다시 q로 옮겨줍니다.
    while sub_q:
        q.append(sub_q.popleft())

    day += 1

for i in range(n):
    for j in range(m):
        tomato = grid[i][j]
        if tomato == -1:
            continue
        # 토마토가 익지 않았다면 -1 출력 후 종료
        if tomato == 0:
            print(-1)
            exit()

print(day)
