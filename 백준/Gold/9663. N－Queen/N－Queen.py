import time

start = time.time()
n = int(input())
availability_grid = [[0 for _ in range(n)] for _ in range(n)]
ans = 0


def color(r, c):
    # c열을 모두 색칠합니다.
    # r,c의 대각방향의 보드에는 모두 색칠합니다.
    availability_grid[r][c] += 1
    # 수직 색칠
    for i in range(r+1, n):
        availability_grid[i][c] += 1
    # 대각(좌측) 색칠
    acc = 1
    while r + acc < n and c - acc >= 0:
        availability_grid[r+acc][c-acc] += 1
        acc += 1
    # 대각(우측) 색칠
    acc = 1
    while r + acc < n and c + acc < n:
        availability_grid[r+acc][c+acc] += 1
        acc += 1


def erase(r, c):
    # c열을 모두 지웁니다.
    # r,c의 대각방향의 보드를 모두 지웁니다.
    availability_grid[r][c] -= 1
    # 수직 색칠
    for i in range(r+1, n):
        availability_grid[i][c] -= 1
    # 대각(좌측) 색칠
    acc = 1
    while r + acc < n and c - acc >= 0:
        availability_grid[r+acc][c-acc] -= 1
        acc += 1
    # 대각(우측) 색칠
    acc = 1
    while r + acc < n and c + acc < n:
        availability_grid[r+acc][c+acc] -= 1
        acc += 1


def back(cnt):
    if cnt == n:
        global ans
        ans += 1
        return
    for i in range(n):
        # 가능한 경우
        if availability_grid[cnt][i] == 0:
            color(cnt, i)
            back(cnt + 1)
            erase(cnt, i)


back(0)
print(ans)
