import sys
import math
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
grid = [[0 for _ in range(m+1)]] + \
    [[0] + list(map(int, input().rstrip())) for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]


# dp[i][j]는 0,0부터 i,j까지의 누적합을 의미
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + grid[i][j]

# 가장 큰 정사각형을 dp 테이블을 참조하며 구할 수 있다.
# i, j가 정사각형의 좌상단 모서리라고 가정하면, k가 정사각형의 길이라고 할 때,
# i, j부터 i+k, j+k의 누적합은 k^2이 되어야 한다
# i, j부터 i+k, j+k의 누적합은 다음과 같은 식으로 구할 수 있다.
# dp[i+k][j+k] - dp[i-1][j+k] - dp[i+k][j-1] + dp[i-1][j-1]
# 최적화를 위해 k는 math.sqrt(ans) 부터 하나씩 늘려간다
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if grid[i][j] == 0:
            continue
        elif ans == 0:
            ans = 1
        boundary = min(n - i, m - j)
        for k in range(ans, boundary + 1):
            expected = (k+1) ** 2
            area = dp[i+k][j+k] - dp[i-1][j+k] - dp[i+k][j-1] + dp[i-1][j-1]
            if expected == area:
                ans = max(ans, k + 1)
            else:
                break

print(ans ** 2)
