import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().rstrip().split()))
upper = max(trees)
lower = 0

ans = 0
while upper >= lower:
    mid = (upper + lower) // 2
    height_sum = 0
    # mid로 잘랐을 때 얻는 높이 구하기
    for height in trees:
        if mid < height:
            height_sum += height - mid
    # 현재 mid가 정답일 가능성이 있을 때
    if height_sum >= m:
        ans = max(ans, mid)
        lower = mid + 1
    else:
        upper = mid - 1

print(ans)
