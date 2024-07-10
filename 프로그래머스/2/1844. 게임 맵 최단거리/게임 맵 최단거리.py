import sys
from collections import deque
INVALID = -1

def solution(maps):
    n, m = len(maps), len(maps[0])
    # (1,1) -> (n,m)으로 bfs를 진행하고 거리를 반환. 갈 수 없으면 -1 반환
    visited = [[False for _ in range(m)] for _ in range(n)]
    distances = [[INVALID for _ in range(m)] for _ in range(n)]
    dxdys = ((0, 1), (0, -1), (1, 0), (-1, 0))
    
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    distances[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxdys:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if maps[nx][ny] == 0 or visited[nx][ny]: continue
            # 방문
            queue.append((nx, ny))
            visited[nx][ny] = True
            distances[nx][ny] = distances[x][y] + 1
    
    return distances[n-1][m-1]