from collections import deque
import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

n, m = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip())) for _ in range(n)]
visited_from_start = [[0 for _ in range(m)] for _ in range(n)]
visited_from_end = [[0 for _ in range(m)] for _ in range(n)]
dist = [[[INT_MAX, INT_MAX] for _ in range(m)] for _ in range(n)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
candidates = []

# 0,0에서 bfs 시작
# 0을 타면서 bfs를 진행함
# 1을 만나는 경우 queue에 삽입하지는 않고 dist[0]값만 변경

# n-1,m-1에서 bfs 시작
# 0을 타면서 bfs를 진행함
# 1을 만나는 경우 queue에 삽입하지는 않고 dist[1]값만 변경
# dist[1]을 변경하고 만약 dist[0]이 INT_MAX가 아니라면 그것또한 답의 후보

# 정답 = max(벽을 하나도 뚫지 않은 경우, 벽을 하나 뚫은 경우)
q = deque()
visited_from_start[0][0] = 1
q.append((0, 0))
dist[0][0][0] = 1

cnt = 1
while q:
    cnt += 1
    for _ in range(len(q)):
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            # 방문하지 않은 경우에만...
            if not visited_from_start[ni][nj]:
                # 벽인 경우엔 기록, 방문 처리만 하고 큐에 삽입하진 않음
                if grid[ni][nj]:
                    dist[ni][nj][0] = cnt
                # 통과할 수 있는 경우엔 기록, 방문 처리, 큐 삽입 함
                else:
                    dist[ni][nj][0] = cnt
                    q.append((ni, nj))
                visited_from_start[ni][nj] = 1

# 벽을 뚫지 않고도 끝점에 도달했다면 정답 후보
if visited_from_start[-1][-1]:
    candidates.append(dist[-1][-1][0])

visited_from_end[-1][-1] = 1
q.append((n-1, m-1))
dist[-1][-1][1] = 1

cnt = 1
while q:
    cnt += 1
    for _ in range(len(q)):
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            # 방문하지 않은 경우에만...
            if not visited_from_end[ni][nj]:
                # 벽인 경우엔 기록, 방문 처리만 하고 큐에 삽입하진 않음
                # 추가적으로 0,0에서 시작했을 때 방문한 벽이라면 양 쪽의 거리 합 -1이 후보가 됨
                if grid[ni][nj]:
                    dist[ni][nj][1] = cnt
                    if dist[ni][nj][0] != INT_MAX:
                        candidates.append(
                            dist[ni][nj][0] + dist[ni][nj][1] - 1)
                # 통과할 수 있는 경우엔 기록, 방문 처리, 큐 삽입 함
                else:
                    dist[ni][nj][1] = cnt
                    q.append((ni, nj))
                visited_from_end[ni][nj] = 1

if candidates:
    print(min(candidates))
else:
    print(-1)
