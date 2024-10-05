# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
# 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
# 4. 반시계 방향으로 90도 회전한다.
# 5. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 6. 1번으로 돌아간다.

n, m = map(int, input().split())
r, c, d = map(int, input().split())
# d: 0(북), 1(동), 2(남), 3(서)

DIRTY = 0
WALL = 1
CLEANED = 2
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

status = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def out_of_boundary(i, j):
    return i < 0 or j < 0 or i >= n or j >= m

def get_near_dirty(i, j):
    dirty_cnt = 0
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if out_of_boundary(ni, nj):
            continue
        if status[ni][nj] == DIRTY:
            dirty_cnt += 1
    
    return dirty_cnt

def check_backward(i, j, d):
    di, dj = dirs[d]
    ni, nj = i - di, j - dj
    if out_of_boundary(ni, nj) or status[ni][nj] == WALL:
        return False
    return True

def check_forward_dirty(i, j, d):
    di, dj = dirs[d]
    ni, nj = i + di, j + dj
    if out_of_boundary(ni, nj) or status[ni][nj] != DIRTY:
        return False
    return True

while True:
    current_status = status[r][c]
    if current_status == DIRTY:
        status[r][c] = CLEANED
        answer += 1
    # 더러운 칸이 없는 경우
    near_dirty_cnt = get_near_dirty(r, c)
    if not near_dirty_cnt:
        # 한 칸 후진 가능한 경우 방향 유지 및 후진
        if check_backward(r, c, d):
            r, c = r - dirs[d][0], c - dirs[d][1]
        else:
            break
    # 더러운 칸이 있는 경우
    else:
        d = (d - 1) % 4
        # 청소되지 않은 칸이라면 전진
        if check_forward_dirty(r, c, d):
            r, c = r + dirs[d][0], c + dirs[d][1]
            
print(answer)