import sys
from collections import deque

input = sys.stdin.readline
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(i, j, board, visited):
    # 배추가 심어진 곳을 기준으로 bfs
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    n, m = len(board), len(board[0])
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if not board[ni][nj] or visited[ni][nj]: 
                continue
            q.append((ni, nj))
            visited[ni][nj] = True

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    answer = 0
    for _ in range(k):
        i, j = map(int, input().split())
        board[j][i] = 1
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                answer += 1
                bfs(i, j, board, visited)
    print(answer)