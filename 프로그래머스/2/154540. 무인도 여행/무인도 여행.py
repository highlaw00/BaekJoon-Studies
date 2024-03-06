from collections import deque

def solution(maps):
    # n: 가로, m: 세로
    n, m = len(maps), len(maps[0])
    answer = []
    # 상/하/좌/우
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            # 현재 좌표가 'X'라면 스킵
            if maps[i][j] == 'X':
                continue
            if visited[i][j]:
                continue
            # 모든 좌표에서 BFS 실시
            queue.append((i, j))
            foods = 0
            while queue:
                x, y = queue.popleft()
                # 이미 방문했다면 스킵
                if visited[x][y]: continue
                visited[x][y] = True
                foods += int(maps[x][y])
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or maps[nx][ny] == 'X':
                        continue
                    if visited[nx][ny]:
                        continue
                    # 인접한 칸이 방문이 가능한 경우: 큐에 삽입
                    queue.append((nx, ny))
            answer.append(foods)
    
    answer.sort()
    if not len(answer): answer.append(-1)
    return answer