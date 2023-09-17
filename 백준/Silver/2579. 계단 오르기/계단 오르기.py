import sys
input = sys.stdin.readline

# dp[i][0]: i번째 계단에 도착할 때, 이전 계단에서 바로 오는 경우
# dp[i][0] = dp[i-1][1] + vals[i]

# dp[i][1]: i번째 계단에 도착할 때, 2칸 전 계단에서 바로 오는 경우
# dp[i][1] = dp[i-2][0] + vals[i]

n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))
dp = [[0, 0] for _ in range(n+1)]
dp[1][0] = stairs[1]
dp[1][1] = stairs[1]
for i in range(2, n+1):
    dp[i][0] = dp[i-1][1] + stairs[i]
    dp[i][1] = max(dp[i-2]) + stairs[i]

print(max(dp[n]))
