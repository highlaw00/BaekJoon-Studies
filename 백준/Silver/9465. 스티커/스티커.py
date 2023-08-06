import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    scores = []
    for _ in range(2):
        l = [0] + list(map(int, input().rstrip().split()))
        scores.append(l)
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    # dp 테이블 초기 조건 삽입
    for i in range(2):
        dp[i][1] = scores[i][1]

    # dp 테이블 갱신
    for i in range(2, n+1):
        s1 = scores[0][i]
        dp[0][i] = max(dp[1][i-1] + s1, dp[1][i-2] + s1)
        s2 = scores[1][i]
        dp[1][i] = max(dp[0][i-1] + s2, dp[0][i-2] + s2)

    print(max(dp[0][n], dp[1][n]))
