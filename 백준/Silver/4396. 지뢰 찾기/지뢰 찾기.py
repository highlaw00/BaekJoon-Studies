n = int(input())

grid = [list(input()) for _ in range(n)]
open_info = [list(input()) for _ in range(n)]
ans = [['.' for _ in range(n)] for _ in range(n)]
dirs = ((-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1))

is_exploded = False

for i in range(n):
    for j in range(n):
        if open_info[i][j] == 'x':
            if grid[i][j] != '*':
                cnt = 0
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if ni < 0 or nj < 0 or ni >= n or nj >= n:
                        continue
                    if grid[ni][nj] == '*':
                        cnt += 1
                ans[i][j] = str(cnt)
            else:
                is_exploded = True

if is_exploded:
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                ans[i][j] = '*'

for row in ans:
    print(''.join(row))
