from collections import deque
import sys
dirs = ((0,1), (0, -1), (1, 0), (-1, 0))

def solution(maps):
    answer = 0
    x, y = 0, 0
    dest_x, dest_y = 0, 0
    n, m = len(maps), len(maps[0])
    
    # 시작 지점 추출
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                x, y = i, j
            elif maps[i][j] == 'E':
                dest_x, dest_y = i, j
                
    # 시작 지점부터 레버까지 BFS
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue.append((x,y,0))
    isFound = False
    
    while queue:
        i, j, cnt = queue.popleft()
        if visited[i][j]: continue
        visited[i][j] = True
        for (di, dj) in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m or visited[ni][nj]: continue
            if maps[ni][nj] == 'X': continue
            if maps[ni][nj] == 'L': 
                answer += cnt + 1
                x, y = ni, nj
                isFound = True
                break
            queue.append((ni, nj, cnt + 1))
        if isFound: break
    
    # 레버까지 못 간 경우
    if not isFound:
        return -1
    
    # 레버부터 끝까지 BFS
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue.append((x,y,0))
    isFound = False
    
    while queue:
        i, j, cnt = queue.popleft()
        if visited[i][j]: continue
        visited[i][j] = True
        for (di, dj) in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m or visited[ni][nj]: continue
            if maps[ni][nj] == 'X': continue
            if maps[ni][nj] == 'E': 
                answer += cnt + 1
                isFound = True
                break
            queue.append((ni, nj, cnt+1))
        if isFound:
            break
    
    if not isFound:
        return -1
    return answer