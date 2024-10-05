import sys
from collections import deque
INF = -sys.maxsize
input = sys.stdin.readline
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
candidates = []

def bfs(start_i, start_j, board):
    q = deque()
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    dists = [[INF] * m for _ in range(n)]
    q.append((start_i, start_j))
    visited[start_i][start_j] = True
    dists[start_i][start_j] = 0
    
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if visited[ni][nj] or board[ni][nj] == 0: 
                continue
            visited[ni][nj] = True
            dists[ni][nj] = dists[i][j] + 1
            q.append((ni, nj))
    
    # 가장 멀리 있는 방 찾기
    maximum_dist = 0
    maximum_val = 0
    for i in range(n):
        maximum_row_dist = max(dists[i])
        maximum_dist = max(maximum_dist, maximum_row_dist)

    for i in range(n):
        for j in range(m):
            dist = dists[i][j]
            if dist == maximum_dist:
                maximum_val = max(maximum_val, board[start_i][start_j] + board[i][j])
    
    global candidates
    candidates.append((maximum_dist, maximum_val))

# 모든 좌표(0이 아닌)에서 BFS를 수행한다.
# BFS를 수행하며 가장 멀리 있는 방을 찾는다.
# 시작방과 끝방의 합이 가장 큰 경우를 반환한다.

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            continue
        bfs(i, j, board)

candidates.sort(key=lambda x: [-x[0], -x[1]])
if candidates:
    print(candidates[0][1])
else:
    print(0)