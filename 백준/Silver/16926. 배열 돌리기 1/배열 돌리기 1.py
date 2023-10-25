import sys
input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
cnt = 0
while cnt < min(n, m) // 2:
    dir_idx = 0
    i, j = cnt, cnt
    arr = []
    new_arr = []
    visited_loc = []

    while not visited[i][j]:
        arr.append(grid[i][j])
        visited_loc.append((i, j))
        visited[i][j] = True
        di, dj = dirs[dir_idx]
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= n or nj >= m or visited[ni][nj]:
            dir_idx = (dir_idx + 1) % 4
            if dir_idx == 0:
                break
            di, dj = dirs[dir_idx]
            ni, nj = i + di, j + dj
        i, j = ni, nj

    move_cnt = r % len(arr)
    for i in range(len(arr)):
        new_arr.append(arr[(i + move_cnt) % len(arr)])
    for i in range(len(new_arr)):
        x, y = visited_loc[i]
        grid[x][y] = new_arr[i]
    cnt += 1

for row in grid:
    print(' '.join(map(str, row)))
