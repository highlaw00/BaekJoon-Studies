n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n+1)]
dp[0][0] = triangle[0][0]

# dp[i][j] = max(dp[i-1][j] + curr, dp[i-1][j-1] + curr)
# 가장 오른쪽, 가장 왼쪽 예외처리
for i in range(1, n):
    for j in range(i+1):
        curr = triangle[i][j]
        # j가 0일 때 dp[i][j] = dp[i-1][j] + curr
        if j == 0:
            dp[i][j] = dp[i-1][j] + curr
        # j가 i일 때 dp[i][j] = dp[i-1][j-1] + curr
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + curr
        else:
            dp[i][j] = max(dp[i-1][j] + curr, dp[i-1][j-1] + curr)

print(max(dp[-1]))
