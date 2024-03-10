from collections import deque

def solution(board):
    answer = -1
    # 시작 위치, 도착 위치 찾기
    s_x, s_y = 0, 0
    d_x, d_y = 0, 0
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                s_x, s_y = i, j
            if board[i][j] == 'G':
                d_x, d_y = i, j
    
    # 큐, 방문 여부 저장
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    dxdy = ((1, 0), (-1, 0), (0, 1), (0, -1))
    queue.append((s_x, s_y, 0))
    
    # BFS 실시
    while queue:
        x, y, cnt = queue.popleft()
        if board[x][y] == 'G':
            answer = cnt
            break
        if visited[x][y]: continue
        visited[x][y] = True
        # 다음 위치가 벽이거나 보드의 끝일때까지 이동하기
        for dx, dy in dxdy:
            weight = 1
            while True:
                nx, ny = x + weight * dx, y + weight * dy
                # 다음 위치가 보드의 끝인 경우 (Out of bound)
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    nx, ny = x + (weight - 1) * dx, y + (weight - 1) * dy
                    break
                # 다음 위치가 벽인 경우
                if board[nx][ny] == 'D':
                    nx, ny = x + (weight - 1) * dx, y + (weight - 1) * dy
                    break
                weight += 1
                
            # 미끄러져 도착한 위치를 이미 방문했다면 무시
            if visited[nx][ny]: continue
            # BFS 진행
            queue.append((nx, ny, cnt + 1))
            
    # 방문 여부 배열 확인 후 정답 리턴
    return answer