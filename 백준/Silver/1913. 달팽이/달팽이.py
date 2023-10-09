n = int(input())
target = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]
numbers_map = {i: False for i in range(1, n*n + 1)}
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
curr_dir = 0
i, j = 0, 0
curr_num = n*n

while curr_num >= 1:
    grid[i][j] = curr_num
    numbers_map[curr_num] = (i, j)
    curr_num -= 1
    di, dj = dirs[curr_dir]
    ni, nj = i + di, j + dj
    if ni < 0 or nj < 0 or ni >= n or nj >= n or grid[ni][nj] != 0:
        curr_dir = (curr_dir + 1) % 4
        di, dj = dirs[curr_dir]
        ni, nj = i + di, j + dj
    i, j = ni, nj

for row in grid:
    print(' '.join(map(str, row)))

target_loc = numbers_map[target]
target_i, target_j = target_loc
print(target_i + 1, target_j + 1)
