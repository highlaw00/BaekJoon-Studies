import sys
sys.setrecursionlimit(600*600+100)
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
x, y = 0, 0
# 하우상좌
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

isDiscovered = False
# I를 찾습니다.
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'I':
            x, y = i, j
            isDiscovered = True
            break
    if isDiscovered:
        break


def dfs(i, j):
    global ans, mat

    # 인접한 곳을 탐색
    for di, dj in dirs:
        n_i, n_j = i + di, j + dj
        # out of range라면 바로 continue or 이미 방문했다면 continue
        if (n_i < 0 or n_j < 0 or n_i >= n or n_j >= m or visited[n_i][n_j]):
            continue
        # 벽이라면 방문하지 않고 continue
        if mat[n_i][n_j] == 'X':
            continue
        # 방문합니다.
        visited[n_i][n_j] = 1
        # 방문한 곳이 만약 P라면 정답 + 1
        if mat[n_i][n_j] == 'P':
            mat[n_i][n_j] = 'O'
            ans += 1
        dfs(n_i, n_j)


# I의 위치에서 깊이 탐색을 시작합니다.
visited[x][y] = 1
dfs(x, y)

if ans != 0:
    print(ans)
else:
    print('TT')
