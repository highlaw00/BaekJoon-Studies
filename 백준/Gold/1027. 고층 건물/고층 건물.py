n = int(input())
heights = list(map(int, input().split()))
ans = 0

def isOver(x1, y1, x2, y2, x3, y3):
    # (x1, y1) 에서 (x2, y2)를 이은 1차 방정식
    gradient = (y2-y1) / (x2-x1)
    return y3 >= gradient * (x3 - x1) + y1

for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j: continue
        isWatchable = True
        # i번째 건물에서 j(0 ~ n)번째 건물과 직선을 긋는다.
        # min(i, j) + 1 ~ max(i, j) - 1 사이의 건물이 직선을 넘어가는지 확인한다.
        # 넘어가면 보이지 않는 것
        for k in range(min(i, j) + 1, max(i, j)):
            if isOver(i, heights[i], j, heights[j], k, heights[k]):
                isWatchable = False
                break
        if isWatchable:
            cnt += 1

    ans = max(ans, cnt)

print(ans)