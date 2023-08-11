# dfs 진행
# DFS 진행하며 다음 칸에 적힌 알파벳이 집합에 존재하는지 확인
# 존재한다면 더이상 진행 x
# dfs 시작할 때 ans 갱신
# 재귀 빠져나오면 set에서 해당 알파벳 삭제 및 길이 -1

# 오답노트: 재귀하면서 -1해줘서 틀림
# 오답노트: 단순한 DFS로는 풀 수 없음

import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
grid = [list(input().rstrip()) for _ in range(r)]
ans = 0
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [False for _ in range(26)]


def dfs(i, j, val):
    val += 1
    global ans
    if val == 26:
        print(val)
        exit()
    ans = max(ans, val)
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= r or nj >= c:
            continue
        next_idx = ord('A') - ord(grid[ni][nj])
        if not visited[next_idx]:
            visited[next_idx] = True
            dfs(ni, nj, val)
            visited[next_idx] = False


visited[ord('A') - ord(grid[0][0])] = True
dfs(0, 0, 0)
print(ans)
