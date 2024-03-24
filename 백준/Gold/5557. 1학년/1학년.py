n = int(input())
numbers = list(map(int,input().split()))
target = numbers[n-1]
numbers = numbers[:n-1]

# dp[i][j] = i번째 항에서 j를 만들 수 있는 경우의 수
dp = [[0 for _ in range(21)] for _ in range(n-1)]

# visited[i][j] = i번째 항에서 i번째 항을 더하거나 뺄 수 있는 수가 저장된 배열 (j = 0 ~ 20)
# visited[i][10] = True : 10에 i번째 항을 더하거나 뺄 수 있다.
visited = [[False for _ in range(21)] for _ in range(n-1)]

dp[0][numbers[0]] = 1
visited[0][numbers[0]] = True

for i in range(1, n-1):
    number = numbers[i]
    for j in range(21):
        if visited[i-1][j]:
            # j + number or j - number
            if 0 <= j + number <= 20:
                dp[i][j + number] += dp[i-1][j]
                visited[i][j + number] = True
            if 0 <= j - number <= 20:
                dp[i][j - number] += dp[i-1][j]
                visited[i][j - number] = True

print(dp[n-2][target])