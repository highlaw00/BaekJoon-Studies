import sys
from collections import deque
input = sys.stdin.readline
INT_MAX = sys.maxsize

n = int(input().rstrip())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
fishes = []
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

# 최초의 상어 위치 및 물고기 정보 기록
r, c = 0, 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            r, c = i, j
            grid[i][j] = 0
        elif grid[i][j] == 0:
            continue
        else:
            # 물고기 정보: (거리, 좌표, 크기, 섭취 여부)
            cost = INT_MAX
            location = (i, j)
            size = grid[i][j]
            is_eaten = False
            fishes.append([cost, location, size, is_eaten])
ans = 0
ate_cnt = 0
curr_size = 2


def bfs(r, c):
    global dists, visited, curr_size
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
                # 자신보다 크면 통과 불가
                # 자신보다 작거나 같으면 통과 가능
                if not visited[ni][nj] and curr_size >= grid[ni][nj]:
                    visited[ni][nj] = True
                    dists[ni][nj] = cost
                    q.append((ni, nj))


while True:
    # 상어 위치에서 BFS 진행하여 물고기 정보 갱신
    visited = [[False for _ in range(n)] for _ in range(n)]
    dists = [[INT_MAX for _ in range(n)] for _ in range(n)]
    visited[r][c] = True
    dists[r][c] = 0
    bfs(r, c)

    # bfs 결과를 토대로 물고기 정보를 갱신 후 정렬
    # 비용을 갱신해야함
    for idx, info in enumerate(fishes):
        _, location, size, _ = info
        i, j = location
        # 접근 가능
        if visited[i][j]:
            fishes[idx][0] = dists[i][j]
        # 접근 불가 시 비용을 INT_MAX로 변환
        else:
            fishes[idx][0] = INT_MAX

    # 정렬을 (거리, 좌표)의 오름차순으로 진행
    fishes.sort(key=lambda x: [x[0], x[1][0], x[1][1]])

    # 먹을 수 있는 후보 중 가장 좋은 후보를 섭취하고 끝냄
    # 없다면 반복문 탈출
    invalid_flag = True
    for idx, info in enumerate(fishes):
        cost, location, size, is_eaten = info
        # 섭취하지 않은 물고기 + 섭취할 수 있는 물고기인 경우에 섭취
        if not is_eaten and curr_size > size and cost != INT_MAX:
            ans += cost
            ate_cnt += 1
            fishes[idx][-1] = True
            r, c = location
            invalid_flag = False
            break

    if invalid_flag:
        break
    # 섭취 후 크기 증가
    if ate_cnt == curr_size:
        curr_size += 1
        ate_cnt = 0

print(ans)
