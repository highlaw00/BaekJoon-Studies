import sys
from collections import deque
input = sys.stdin.readline
INT_MAX = sys.maxsize

n = int(input().rstrip())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

# 최초의 상어 위치 및 물고기 정보 기록
r, c = 0, 0
for i in range(n):
    flag = False
    for j in range(n):
        if grid[i][j] == 9:
            r, c = i, j
            grid[i][j] = 0
            flag = False
            break
    if flag:
        break


def bfs(r, c):
    global dists, visited, curr_size, eatable_fishes, eaten_fishes
    q = deque()
    q.append((r, c))
    cost = 0
    while q:
        cost += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= n or nj >= n:
                    continue
                # 자신보다 작거나 같으면 통과 가능
                if not visited[ni][nj] and curr_size >= grid[ni][nj]:
                    visited[ni][nj] = True
                    dists[ni][nj] = cost
                    q.append((ni, nj))
                    # 먹지 않았으며 먹을 수 있다면 기록
                    if grid[ni][nj] != 0 and curr_size > grid[ni][nj] and (ni, nj) not in eaten_fishes:
                        eatable_fishes.append((cost, (ni, nj)))


ans = 0
ate_cnt = 0
curr_size = 2
eaten_fishes = set()

while True:
    # 상어 위치에서 BFS 진행하여 물고기 정보 갱신
    visited = [[False for _ in range(n)] for _ in range(n)]
    dists = [[INT_MAX for _ in range(n)] for _ in range(n)]
    visited[r][c] = True
    dists[r][c] = 0
    eatable_fishes = []
    bfs(r, c)
    # 먹을 수 있는 물고기를 오름차순 정렬 (비용, row, column)
    eatable_fishes.sort(key=lambda x: [x[0], x[1][0], x[1][1]])

    if eatable_fishes:
        cost, location = eatable_fishes[0]
        i, j = location
        ans += cost
        ate_cnt += 1
        eaten_fishes.add((i, j))
        r, c = i, j
    else:
        break

    # 섭취 후 크기 증가
    if ate_cnt == curr_size:
        curr_size += 1
        ate_cnt = 0

print(ans)
