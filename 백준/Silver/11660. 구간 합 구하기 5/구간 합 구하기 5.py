import sys

n, m = map(int, input().split())

mat = [[0 for _ in range(n + 1)]]
prefix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    mat.append(arr)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1:
            prefix[i][j] = prefix[i][j - 1] + mat[i][j]
        elif j == 1:
            prefix[i][j] = prefix[i - 1][j] + mat[i][j]
        else:
            prefix[i][j] = (
                prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i][j]
            )

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(
        prefix[x2][y2]
        - prefix[x2][y1 - 1]
        - prefix[x1 - 1][y2]
        + prefix[x1 - 1][y1 - 1]
    )
