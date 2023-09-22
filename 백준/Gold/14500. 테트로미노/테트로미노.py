import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 0, 0 ~ 0,3 and 3,0
r0c0 = (0, 0)
r0c1 = (0, 1)
r0c2 = (0, 2)
r0c3 = (0, 3)
r1c0 = (1, 0)
r2c0 = (2, 0)
r3c0 = (3, 0)

r1c1 = (1, 1)
r1c2 = (1, 2)
r2c1 = (2, 1)

case1 = [(r0c0, r0c1, r0c2, r0c3), (r0c0, r1c0, r2c0, r3c0)]
case2 = [(r0c0, r0c1, r1c0, r1c1)]
case3 = [(r0c0, r1c0, r2c0, r2c1), (r0c0, r1c0, r0c1, r0c2),
         (r0c0, r0c1, r1c1, r2c1), (r0c2, r1c0, r1c1, r1c2),
         (r0c1, r1c1, r2c0, r2c1), (r0c0, r1c0, r1c1, r1c2),
         (r0c0, r0c1, r1c0, r2c0), (r0c0, r0c1, r0c2, r1c2)]
case4 = [(r0c0, r1c0, r1c1, r2c1), (r0c1, r0c2, r1c0, r1c1),
         (r0c1, r1c0, r1c1, r2c0), (r0c0, r0c1, r1c1, r1c2)]
case5 = [(r0c0, r0c1, r0c2, r1c1), (r0c1, r1c0, r1c1, r2c1),
         (r0c1, r1c0, r1c1, r1c2), (r0c0, r1c0, r1c1, r2c0)]

cases = [case1, case2, case3, case4, case5]


def is_in_range(i, j):
    return not (i < 0 or j < 0 or i >= n or j >= m)


ans = 0

for i in range(n):
    for j in range(m):
        for case in cases:
            for dirs in case:
                cnt = 0
                summation = 0
                for dir in dirs:
                    di, dj = dir
                    ni, nj = i + di, j + dj
                    if is_in_range(ni, nj):
                        cnt += 1
                        summation += grid[ni][nj]
                    else:
                        break
                # 가능한 경우
                if cnt == 4:
                    ans = max(ans, summation)

print(ans)
