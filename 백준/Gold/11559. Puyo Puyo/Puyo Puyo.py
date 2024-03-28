from collections import deque
grid = [list(input()) for _ in range(12)]
n = 12
m = 6
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

# 뿌요 뿌요

# 2. 터트리기
# 3. 중력의 영향을 받아 내려오기
# 4. 터지는 뿌요 그룹 없을 때 까지 1~3 반복

def bfs(grid, visited, i, j):
    global n, m, dirs
    q = deque()
    visited = [[visited[i][j] for j in range(m)] for i in range(n)]
    q.append((i, j))
    start_color = grid[i][j]
    cnt = 0
    
    while q:
        x, y = q.popleft()
        if visited[x][y]: continue
        visited[x][y] = True
        cnt += 1
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if visited[nx][ny]: continue
            # 처음 블록과 동일 색상이면 큐에 삽입
            if grid[nx][ny] == start_color:
                q.append((nx, ny))
    
    return cnt, visited

# 1. 터지는 뿌요 그룹 찾기 (여러개도 가능)
def find(grid):
    visited = [[False for _ in range(m)] for _ in range(n)]
    group_cnt = 0
    isFirst = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.': continue
            if visited[i][j]: continue
            # 방문하지 않고 뿌요 블럭 찾음 -> bfs 시작
            block_cnt, new_visited = bfs(grid, visited, i, j)
            if block_cnt >= 4:
                if isFirst: 
                    group_cnt += 1
                    isFirst = False
                visited = new_visited

    return group_cnt, visited

def clear(grid, visited):
    global n, m
    for i in range(n):
        for j in range(m):
            # 터지는 경우
            if visited[i][j]:
                grid[i][j] = '.'

def gravity(grid):
    global n, m
    for i in range(n-2, -1, -1):
        for j in range(m):
            # 중력 작용시키기
            if grid[i][j] != '.':
                # 떨어질 칸 찾기
                ni, nj = i, j
                while ni + 1 < n and grid[ni + 1][nj] == '.':
                    ni += 1
                if ni == i and nj == j: continue
                grid[ni][nj] = grid[i][j]
                grid[i][j] = '.'
                    

def sol(grid):
    ans = 0
    while True:
        cnt, visited = find(grid)
        ans += cnt
        if cnt > 0: 
            clear(grid, visited)
            gravity(grid)
        else:
            break
    
    return ans

gravity(grid)
ans = sol(grid)
print(ans)