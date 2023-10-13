grid = [list(map(int, input().split())) for _ in range(5)]
visited = [[False for _ in range(5)]for _ in range(5)]
calls = [list(map(int, input().split())) for _ in range(5)]

d = dict()
for i in range(5):
    for j in range(5):
        d[grid[i][j]] = (i, j)

cnt = 0
ans = 0
isDone = False
bingo_cnt = 0

for call in calls:
    for num in call:
        bingo_cnt = 0
        cnt += 1
        i, j = d[num]
        visited[i][j] = True
        # visited의 대각과 수직 수평을 조사
        # 수평
        for k in range(5):
            if True == visited[k][0] == visited[k][1] == visited[k][2] == visited[k][3] == visited[k][4]:
                bingo_cnt += 1
            if True == visited[0][k] == visited[1][k] == visited[2][k] == visited[3][k] == visited[4][k]:
                bingo_cnt += 1

        isCrossed = True
        for k in range(5):
            if visited[k][k] != True:
                isCrossed = False
                break
        if isCrossed:
            bingo_cnt += 1

        isCrossed = True
        for k in range(5):
            if visited[k][4-k] != True:
                isCrossed = False
                break
        if isCrossed:
            bingo_cnt += 1

        if bingo_cnt >= 3:
            ans = cnt
            isDone = True
            break
    if isDone:
        break

print(ans)
