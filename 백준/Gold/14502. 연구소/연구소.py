# 지도가 주어지면 0의 위치를 기록한다.
# 0의 위치 중 3개를 뽑아서 해당 위치에 벽을 세운 뒤 전체에 대해 BFS 탐색을 한다.
# BFS 탐색을 하며 만난 0을 카운트하고, 초기에 뽑은 0의 개수 - 만난 0의 개수의 최대값을 찾는다.
# 0위치 기록 => O(NM), 3개 뽑는 연산 => O(NM), BFS 탐색 => O(NM)
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
viruses = []
zeros = []
candidates = []
q = deque()
ans = 0

for i in range(n):
    for j in range(m):
        # 0의 위치 기록
        if grid[i][j] == 0:
            zeros.append((i, j))
            continue
        elif grid[i][j] == 2:
            viruses.append((i, j))


def bfs(visited):
    ret = 0
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if grid[ni][nj] == 0 and not visited[ni][nj]:
                visited[ni][nj] = 1
                ret += 1
                q.append((ni, nj))
    return ret

# 0의 위치 3개 뽑는 백트래킹


def back(cnt, idx):
    global ans
    if cnt == 3:
        # 여기서 BFS 진행
        # candidates에 존재하는 인덱스를 참조해 grid의 값을 1로 변환
        for i, j in candidates:
            grid[i][j] = 1
        visited = [[0 for _ in range(m)] for _ in range(n)]
        infected = 0
        for i, j in viruses:
            q.append((i, j))
            infected += bfs(visited)
        # 전체 0의 개수 - 탐색하며 방문한 0의 개수 => 탐색하지 않은 0의 개수(안전 영역의 넓이)
        ans = max(ans, len(zeros) - infected - 3)
        # 탐색 완료하고 grid 값 반환
        for i, j in candidates:
            grid[i][j] = 0

        return
    for i in range(idx, len(zeros)):
        candidates.append(zeros[i])
        back(cnt+1, i+1)
        candidates.pop()


back(0, 0)

print(ans)
