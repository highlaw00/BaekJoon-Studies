# 빙산들은 주변에 존재하는 바닷물에 의해 녹는다.
# 1년에 빙산들이 녹는 양은 사면에 둘러쌓인 바닷물의 양과 똑같다.
# 빙산이 두 덩어리로 나눠지는 최초의 시간을 구하라.

# 시뮬레이션?
# 데이터가 90000개, 정수가 들어가는 데이터는 10000개
# 들어가는 값은 10으로 시뮬레이션이 가능하네요

# 입력
# 빙산의 위치를 모두 입력 받는다 + 사면에 둘러쌓인 바닷물의 개수
# 바닷물의 개수만큼 값을 빼주고, 빙산을 모두 갱신합니다
# BFS를 모든 빙산에 대해 진행하는데, 이 때 색을 칠합니다 (원래 색은 1임)
# 빙산이 만약 두 덩어리 이상이라면, 색의 종류가 2개 이상이 됩니다
# 따라서 그 때의 시간을 출력하면 됨
# BFS 언제 끝나는가? 남은 빙하가 없을 때 끝낸다

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
icebergs = []
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

# 빙산 탐색
for i in range(n):
    for j in range(m):
        if grid[i][j] != 0:
            cnt = 0
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if grid[ni][nj] == 0:
                    cnt += 1
            icebergs.append([i, j, cnt])

# 빙하가 모두 없어질 때 까지 진행합니다
ans = 0
while icebergs:
    ans += 1
    # 빙하들의 값을 모두 갱신합니다
    temp = []
    melted = []
    for iceberg in icebergs:
        i, j, sea_cnt = iceberg
        grid[i][j] -= sea_cnt
        if grid[i][j] <= 0:
            grid[i][j] = 0
        else:
            temp.append([i, j, cnt])

    # 모두 녹아버린 경우
    if not temp:
        ans = 0
        break

    for idx, val in enumerate(temp):
        i, j, sea_cnt = val
        cnt = 0
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if grid[ni][nj] <= 0:
                cnt += 1
        if sea_cnt != cnt:
            temp[idx][2] = cnt

    # 녹은 후에도 남아있는 빙하에 대해서 BFS 를 진행합니다
    q = deque()
    visited = {(i, j): False for i, j, _ in temp}
    i, j, _ = temp[0]
    visited[(i, j)] = True
    q.append((i, j))

    visited_cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if (ni, nj) in visited and not visited[(ni, nj)] and grid[ni][nj] != 0:
                visited[(ni, nj)] = True
                q.append((ni, nj))
                visited_cnt += 1

    if visited_cnt != len(visited):
        break

    icebergs = temp

print(ans)
