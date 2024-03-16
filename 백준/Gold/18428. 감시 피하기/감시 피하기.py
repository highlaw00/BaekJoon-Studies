n = int(input())
grid = [input().split() for _ in range(n)]
ans = 'NO'
candidates = []
teachers = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'X': candidates.append((i, j))
        elif grid[i][j] == 'T': teachers.append((i, j))

def check():
    global grid, teachers
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    # 선생님을 순회하며 감시가능한지 확인
    for x, y in teachers:
        for dx, dy in dirs:
            weight = 1
            while True:
                nx, ny = x + weight * dx, y + weight * dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n: break
                if grid[nx][ny] == 'O': break
                if grid[nx][ny] == 'S': return False
                weight += 1
    return True

def back(cnt):
    global ans, grid, candidates
    if cnt == 3:
        result = check()
        if result: ans = 'YES'
        return
    for candidate in candidates:
        x, y = candidate
        if grid[x][y] == 'O': continue
        grid[x][y] = 'O'
        back(cnt + 1)
        grid[x][y] = 'X'

back(0)
print(ans)