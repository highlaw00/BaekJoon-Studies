import sys
INVALID = -sys.maxsize

# n = 세로, m = 가로
def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    for puddle in puddles:
        x, y = puddle
        dp[y-1][x-1] = INVALID
    
    dp[0][0] = 1
    
    # 0,0 ~ 0, m-1 까지 초기화
    for i in range(1, m):
        if dp[0][i] == INVALID: break
        dp[0][i] = dp[0][i-1]
    
    # 0,0 ~ n-1,0 까지 초기화
    for i in range(1, n):
        if dp[i][0] == INVALID: break
        dp[i][0] = dp[i-1][0]
        
    # 1,1 ~ n-1, m-1 까지 초기화
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == INVALID: continue
            
            # (i-1, j) 와 (i, j-1) 확인
            cnt = 0
            if dp[i-1][j] != INVALID:
                cnt += dp[i-1][j]
            if dp[i][j-1] != INVALID:
                cnt += dp[i][j-1]
            
            dp[i][j] = cnt % 1_000_000_007
    
    answer = dp[n-1][m-1]
    
    return answer