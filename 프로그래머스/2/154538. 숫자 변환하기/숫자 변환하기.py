# dp[i] = X에서 i로 변환하기 위한 최소 연산 횟수
# dp[i+n] = min(dp[i+n], dp[i] + 1)
# dp[i*2] = min(dp[i*2], dp[i] + 1)
# dp[i*3] = min(dp[i*3], dp[i] + 1)
import sys
INT_MAX = sys.maxsize

def solution(x, y, n):
    dp = [INT_MAX for _ in range(y+1)]
    dp[x] = 0
    
    for i in range(x, y):
        if i+n <= y:
            dp[i+n] = min(dp[i+n], dp[i] + 1)
        if i*2 <= y:
            dp[i*2] = min(dp[i*2], dp[i] + 1)
        if i*3 <= y:
            dp[i*3] = min(dp[i*3], dp[i] + 1)
    
    if dp[y] == INT_MAX:
        return -1
    
    return dp[y]