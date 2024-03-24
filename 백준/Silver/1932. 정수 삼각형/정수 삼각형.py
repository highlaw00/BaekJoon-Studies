n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
# dp[i][j] = i,j번째 숫자까지 오는 경로 중 선택된 수의 합이 최대인 경로
dp = [[0 for _ in range(i)] for i in range(1, n+1)]

dp[0][0] = triangle[0][0]

# 1,0 ~ n-1,0 채우기
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + triangle[i][0]

# 1,1 ~ n-1, n-1 채우기
for i in range(1, n):
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]

if n >= 3:
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    
print(max(dp[n-1]))