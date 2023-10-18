import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
moves = [tuple(map(int, input().rstrip().split())) for _ in range(m)]
dirs = ((0, -1), (-1, -1), (-1, 0), (-1, 1),
        (0, 1), (1, 1), (1, 0), (1, -1))
cross_dirs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

for move in moves:
    # 마지막 위치 집합 초기화
    last_cloud = set()

    d, s = move
    d = d - 1
    direction = dirs[d]

    # 모든 구름 이동
    for idx, cloud in enumerate(clouds):
        # 구름 이동
        i, j = cloud
        di, dj = direction
        ni, nj = (i + di * s) % n, (j + dj * s) % n

        # 해당 위치에 물 증가
        grid[ni][nj] += 1
        # 구름의 마지막 위치 기록 (물이 증가한 위치)
        last_cloud.add((ni, nj))

    for i, j in last_cloud:
        # 물복사 버그
        cnt = 0
        for cross_dir in cross_dirs:
            di, dj = cross_dir
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue
            if grid[ni][nj] >= 1:
                cnt += 1

        grid[i][j] += cnt

    # 배열 초기화
    clouds = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and (i, j) not in last_cloud:
                clouds.append([i, j])
                grid[i][j] -= 2

ans = 0
for i in range(n):
    for j in range(n):
        ans += grid[i][j]
print(ans)
