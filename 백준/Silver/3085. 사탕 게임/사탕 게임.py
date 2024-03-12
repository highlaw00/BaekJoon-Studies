n = int(input())
grid = [list(input()) for _ in range(n)]
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
ans = 0

def check(grid):
    global n
    ret = 0
    
    # 행 확인
    for i in range(n):
        s, e = 0, 0
        cand = 0
        # end가 out of bound 될 때 까지
        while e < n:
            if grid[i][s] == grid[i][e]:
                cand += 1
                ret = max(ret, cand)
                e += 1
            else:
                ret = max(ret, cand)
                cand = 0
                s = e

    # 열 확인
    for i in range(n):
        s, e = 0, 0
        cand = 0
        # end가 out of bound 될 때 까지
        while e < n:
            if grid[s][i] == grid[e][i]:
                cand += 1
                ret = max(ret, cand)
                e += 1
            else:
                ret = max(ret, cand)
                cand = 0
                s = e
    
    return ret
                
for i in range(n):
    for j in range(n):
        # 인접한 다른 색깔의 사탕 교체
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= n: continue
            if grid[i][j] == grid[ni][nj]: continue
            
            # 교체
            grid[i][j], grid[ni][nj] = grid[ni][nj], grid[i][j]
            
            # 가장 긴 연속 부분 확인
            ans = max(ans, check(grid))
            
            # 원복
            grid[i][j], grid[ni][nj] = grid[ni][nj], grid[i][j]
    
print(ans)