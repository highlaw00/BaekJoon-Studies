dp = [0 for _ in range(101)]

for i in range(1, 101):
    if i <= 3:
        dp[i] = 1
    elif i <= 5:
        dp[i] = 2
    else:
        dp[i] = dp[i-1] + dp[i-5]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
