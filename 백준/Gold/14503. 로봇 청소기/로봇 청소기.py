n, m = map(int, input().split())
i, j, d = map(int, input().split())

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
is_wall = [list(map(int, input().split())) for _ in range(n)]
is_cleaned = [[False for _ in range(m)] for _ in range(n)]

ans = 0

while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
    if not is_cleaned[i][j]:
        is_cleaned[i][j] = True
        ans += 1
    
    # 현재 칸의 주변 4칸 중 조사
    cleaned_cnt, available_room_cnt = 0, 0
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= n or nj >= m:
            continue
        if is_wall[ni][nj]:
            continue
        available_room_cnt += 1
        if is_cleaned[ni][nj]: 
            cleaned_cnt += 1
    
    # 모두 청소된 경우
    if cleaned_cnt == available_room_cnt:
        back_di, back_dj = dirs[(d + 2) % 4]
        ni, nj = i + back_di, j + back_dj
        # 후진 할 수 없으면 작동 멈춤
        if ni < 0 or nj < 0 or ni >= n or nj >= m or is_wall[ni][nj]: 
            break
        # 바라보는 방향 유지하며 후진 할 수 있다면 후진하고 1번으로 돌아감
        else:
            i, j = ni, nj
            continue
    
    # 청소되지 않은 빈 칸이 있는 경우...
    # 청소되지 않은 빈 칸을 찾을 때 까지 반시계 방향으로 90도 회전
    # 이후 한 칸 전진
    while True:
        d = (d-1) % 4
        di, dj = dirs[d]
        ni, nj = i + di, j + dj

        if ni < 0 or nj < 0 or ni >= n or nj >= m or is_wall[ni][nj]: 
            continue
        if not is_cleaned[ni][nj]:
            i, j = ni, nj
            break

print(ans)