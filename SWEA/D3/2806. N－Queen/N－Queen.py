def check(k, x, y, grid):
    # 좌상 대각선 확인
    # x-1, y-1
    for i in range(k):
        if x-i < 0 or y-i < 0: break
        if grid[x-i][y-i]: return False
    
    # 우상 대각선 확인
    # x+1, y+1
    for i in range(k):
        if x-i >= k or y+i >= k: break
        if grid[x-i][y+i]: return False

    # 수직선 확인
    for i in range(k):
        if x-i < 0: break
        if grid[x-i][y]: return False
    
    return True
    

def back(k, cnt, grid):
    if cnt == k:
        global answer
        answer += 1
        return
    # cnt열에 퀸을 둘 수 있는지 확인
    for i in range(k):
        # 현재 자리에 두는게 가능한 경우 둔다.
        # 퀸을 위치시킨 뒤 다음 행으로 재귀
        if check(k, cnt, i, grid):
            grid[cnt][i] = True
            back(k, cnt+1, grid)
            grid[cnt][i] = False

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    answer = 0
    grid = [[False for _ in range(n)] for _ in range(n)]
    back(n, 0, grid)
    print(f"#{test_case} {answer}")