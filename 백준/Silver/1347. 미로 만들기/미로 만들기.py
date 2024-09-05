n = int(input())
s = input()

i, j = 0, 0
# 남, 동, 북, 서. 오른쪽 90도 회전: -1 / 왼쪽 90도 회전: +1
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
current_dir = 0
visited = set()

visited.add((i, j))

for ch in s:
    if ch == 'F':
        # 한 칸 이동 후 위치 삽입
        di, dj = dirs[current_dir]
        i, j = i + di, j + dj
        visited.add((i, j))
    elif ch == 'L':
        current_dir = (current_dir + 1) % 4
    elif ch == 'R':
        current_dir = (current_dir - 1) % 4

min_i, min_j = 0, 0
max_i, max_j = 0, 0
for i, j in visited:
    min_i = min(min_i, i)
    min_j = min(min_j, j)
    max_i = max(max_i, i)
    max_j = max(max_j, j)

answer = [['#' for _ in range(max_j - min_j + 1)] for _ in range(max_i - min_i + 1)]
for i, j in visited:
    ni, nj = i + abs(min_i), j + abs(min_j)
    answer[ni][nj] = '.'

for row in answer:
    print(''.join(row))