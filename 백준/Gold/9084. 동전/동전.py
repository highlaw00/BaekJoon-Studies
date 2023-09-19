import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().rstrip().split()))
    m = int(input())

    # dp[i] = (현재까지 주어진 동전으로) i원을 만들 수 있는 가짓수
    dp = [0 for _ in range(m+1)]
    for val in coins:
        if val > m:
            continue
        dp[val] += 1
        for i in range(val+1, m+1):
            # dp[i] = dp[i] + dp[i-val]
            # dp[i]는 기존의 가짓수
            # +
            # (i-val)에서 val 더하면 i가 되기 때문에 dp[i-val]
            dp[i] = dp[i] + dp[i - val]

    print(dp[m])
