# 치즈 내부 공간의 공기 = 상관 없음
# 치즈 외부 공간의 공기 = 실내 온도의 공기

# 1. 그리드 입력
# 2. 1,1에서 bfs하여 실내 공기 표시
# 3. 이 후 치즈와 내부 공기 표시
# 4. 모든 치즈를 완전탐색하며 4면에 실내 공기가 존재하는지 파악
# 5. 2개 이상 존재하는 것을 기록
# 6. 완전탐색이 끝나면 5번에서 기록한 것을 모두 삭제
# 7. 만약 기록한 것이 없다면 모두 녹은 것

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

# 0,0에서 bfs하여 실내 공기 표시 => 2로 표시함


def bfs_air():
    global grid
    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    q.append((0, 0))
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if not visited[ni][nj] and (grid[ni][nj] == 0 or grid[ni][nj] == 2):
                visited[ni][nj] = 1
                grid[ni][nj] = 2
                q.append((ni, nj))


grid[0][0] = 2
bfs_air()

# 치즈 위치 파악 및 맞닿은 공기 파악
cheeses = dict()
about_to_melt = dict()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            cnt = 0
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= n or nj >= m:
                    continue
                if grid[ni][nj] == 2:
                    cnt += 1
            info = (i, j)
            cheeses[info] = cnt
            if cnt >= 2:
                about_to_melt[info] = cnt


ans = 0
# 남은 치즈가 없어질때까지 진행
while len(cheeses):
    ans += 1
    # 맞닿은 면이 2개 이상인 치즈를 모두 변경해주기
    for info in about_to_melt.keys():
        i, j = info
        grid[i][j] = 2
        del cheeses[info]
    # 치즈가 모두 녹았으니 초기화
    about_to_melt = dict()
    # 치즈가 모두 녹은 뒤 실내 공기 bfs로 갱신하기
    bfs_air()
    # 치즈가 모두 녹은 뒤 남은 치즈 정보 갱신
    for info in cheeses.keys():
        i, j = info
        cnt = 0
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if grid[ni][nj] == 2:
                cnt += 1
        cheeses[info] = cnt
        if cnt >= 2:
            about_to_melt[info] = cnt

print(ans)
