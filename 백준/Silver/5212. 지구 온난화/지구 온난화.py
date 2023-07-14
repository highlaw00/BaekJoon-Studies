r, c = map(int, input().split())
mat = []
# 상하좌우 순
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
indices = []


def check(row, col):
    return 0 <= row and row < r and 0 <= col and col < c


for _ in range(r):
    row = list(map(str, input()))
    mat.append(row)

for i in range(r):
    for j in range(c):
        # 없어지는 섬을 모두 바다로 변경합니다.
        if mat[i][j] == '.':
            continue
        cnt = 0
        for dr, dc in zip(drs, dcs):
            new_r, new_c = i + dr, j + dc
            if not check(new_r, new_c):
                cnt += 1
            elif mat[new_r][new_c] == '.':
                cnt += 1
        if cnt >= 3:
            indices.append([i, j])

for i, j in indices:
    mat[i][j] = '.'

left, right, bottom, top, = c-1, 0, 0, r-1

for i in range(r):
    for j in range(c):
        if mat[i][j] == 'X':
            left = min(left, j)
            right = max(right, j)
            bottom = max(bottom, i)
            top = min(top, i)

for i in range(top, bottom+1):
    for j in range(left, right+1):
        print(mat[i][j], end='')
    print()
