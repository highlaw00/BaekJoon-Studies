n = int(input())
numbers = list(map(int,input().split()))
target = numbers[n-1]
numbers = numbers[:n-1]

# dp[i][j] = i번째 항에서 j를 만들 수 있는 경우의 수
dp = [[0 for _ in range(21)] for _ in range(n-1)]

dp[0][numbers[0]] = 1

for i in range(1, n-1):
    number = numbers[i]
    for j in range(21):
        if dp[i-1][j]:
            # j + number or j - number
            if 0 <= j + number <= 20:
                dp[i][j + number] += dp[i-1][j]
            if 0 <= j - number <= 20:
                dp[i][j - number] += dp[i-1][j]

print(dp[n-2][target])