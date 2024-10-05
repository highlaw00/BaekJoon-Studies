import sys
INVALID = -sys.maxsize

def solution(n):
    answer = [[INVALID for _ in range(n)] for _ in range(n)]
    
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = 0
    x, y = 0, 0
    
    for i in range(1, n*n+1):
        answer[x][y] = i
        dx, dy = dirs[direction]
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n or answer[nx][ny] != INVALID:
            direction = (direction + 1) % 4
            dx, dy = dirs[direction]
            nx, ny = x + dx, y + dy
        x, y = nx, ny
    
    return answer