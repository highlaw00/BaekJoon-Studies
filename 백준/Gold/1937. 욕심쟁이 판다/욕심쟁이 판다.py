import sys
input = sys.stdin.readline
sys.setrecursionlimit(26_000)

# DP 테이블을 DFS하며 진행
n = int(input().rstrip())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]

# dp[i][j] = (i,j)에서 방문 할 수 있는 가장 많은 칸
# dp[i][j] = (i,j)에서 dfs 진행, 인접한 블록을 방문하며 dp[i+k][j+t]가 이미 기록되었다면
dp = [[0 for _ in range(n)] for _ in range(n)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))


def dfs(i, j):
    if dp[i][j] == 0:
        dp[i][j] = 1
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= n or nj >= n:
            continue
        # 이동할 수 있다면 dfs 진행
        if grid[i][j] >= grid[ni][nj]:
            continue
        if dp[ni][nj] == 0:
            dfs(ni, nj)
        dp[i][j] = max(dp[i][j], dp[ni][nj] + 1)


for i in range(n):
    for j in range(n):
        dfs(i, j)

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)
