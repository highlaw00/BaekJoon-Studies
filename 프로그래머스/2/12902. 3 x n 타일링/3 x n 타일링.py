def solution(n):
    dp = [0 for _ in range(5_001)]
    
    dp[2] = 3
    
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3 + 2
        for j in range(4, i, 2):
            dp[i] += 2 * dp[i-j]
        dp[i] = dp[i] % 1_000_000_007
    
    return dp[n]