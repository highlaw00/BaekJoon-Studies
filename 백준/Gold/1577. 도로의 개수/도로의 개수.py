import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
k = int(input().rstrip())
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
is_available = [[[] for _ in range(n+1)] for _ in range(m+1)]

for _ in range(k):
    a, b, c, d = map(int, input().rstrip().split())
    # a, b => x, y
    b, d = m-b, m-d
    # (a,b)와 (c,d)를 잇는 선분이 공사 중
    # is_available[b][a] 에 (d, c) 삽입
    # is_available[d][c] 에 (b, a) 삽입
    is_available[b][a].append((d, c))
    is_available[d][c].append((b, a))

# i, j => (M, 0) ~ (0, 0)의 dp 갱신
for i in range(m-1, -1, -1):
    # 이전의 길이 공사중이라면 dp 값 0
    j = 0
    if (i+1, j) in is_available[i][j]:
        dp[i][j] = 0
    else:
        if dp[i+1][j] == 0 and i+1 != m:
            dp[i][j] = 0
        else:
            dp[i][j] = 1

# i, j => (M, 0) ~ (M, N)의 dp 갱신
for j in range(1, n+1):
    i = m
    if (i, j-1) in is_available[i][j]:
        dp[i][j] = 0
    else:
        if dp[i][j-1] == 0 and j != 1:
            dp[i][j] = 0
        else:
            dp[i][j] = 1

# i => n-1 ~ 0 까지
# j => 1 ~ m 까지

for i in range(m-1, -1, -1):
    for j in range(1, n+1):
        # 왼쪽 길과 아래길 모두 막힌 경우 => dp[i][j] = 0
        # 왼쪽 길만 막힌 경우 => dp[i][j] = dp[i+1][j]
        # 아래쪽 길만 막힌 경우 => dp[i][j] = dp[i][j-1]
        # 둘 다 아닌 경우 => dp[i][j] = dp[i-1][j] + dp[i][j-1]

        is_left_constructing = (i, j-1) in is_available[i][j]
        is_lower_constructing = (i+1, j) in is_available[i][j]

        if is_left_constructing and is_lower_constructing:
            dp[i][j] = 0
        elif is_left_constructing:
            dp[i][j] = dp[i+1][j]
        elif is_lower_constructing:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = dp[i+1][j] + dp[i][j-1]

print(dp[0][-1])
