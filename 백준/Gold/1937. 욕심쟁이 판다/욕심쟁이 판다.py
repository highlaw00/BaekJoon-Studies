import sys
import heapq
sys.setrecursionlimit(26_000)
input = sys.stdin.readline

n = int(input().rstrip())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
# dp[i][j] = i,j에서 출발했을 때 도달할 수 있는 칸의 수
# dp[i][j] = (val, dirs)
# 도달할 수 있는 칸의 수를 점진적으로 증가시킵니다
dp = [[[1, []] for _ in range(n)] for _ in range(n)]
# dp 갱신을 위한 우선순위 큐
pq = []

# dp 테이블 초기화
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

for i in range(n):
    for j in range(n):
        movable = False
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue
            # 현재 값이 인접 값보다 작으면 이동 가능
            if grid[i][j] < grid[ni][nj]:
                movable = True
                dp[i][j][1].append((di, dj))
        if movable:
            dp[i][j][0] = 2
            heapq.heappush(pq, (len(dp[i][j][1]), i, j))


def dfs(i, j):
    directions = dp[i][j][1]

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if len(dp[ni][nj][1]) != 0:
            dfs(ni, nj)
        dp[i][j][0] = max(dp[i][j][0], dp[ni][nj][0] + 1)

    # 주변을 다 방문한 뒤에는 연결 경로 삭제
    dp[i][j][1] = []


# 방문할 수 있는 인접한 블록의 수가 가장 적은 것부터 꺼내며 탐색합니다
while pq:
    len_dirs, i, j = heapq.heappop(pq)
    directions = dp[i][j][1]
    # 인접 블록 수가 갱신되었다면 continue
    if len_dirs != len(directions):
        continue

    dfs(i, j)

ans = 1
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j][0])

print(ans)
