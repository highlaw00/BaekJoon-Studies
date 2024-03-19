n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1

# bottom-up
for i in range(2, n+1):
    # dp[i][j] = 길이가 i이며 시작 수 가 j인 오르막 수의 개수
    for j in range(10):
        # dp[i][j] = sum(dp[i-1][k]) k = (j ~ 10)
        summation = 0
        for k in range(j, 10):
            summation += dp[i-1][k]
        dp[i][j] = summation % 10_007

print(sum(dp[n]) % 10_007)