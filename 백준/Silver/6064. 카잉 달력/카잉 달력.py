import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, n, x, y = map(int, input().rstrip().split())
    # max(m,n)의 잉여집합
    x, y = x - 1, y - 1
    ans = -1
    if m >= n:
        bigger = m
        bigger_rem = x
        smaller = n
        smaller_rem = y
    else:
        bigger = n
        bigger_rem = y
        smaller = m
        smaller_rem = x
    seed = bigger_rem
    while seed <= m * n:
        # seed를 작은것으로 나눠보고 나머지 확인
        if seed % smaller == smaller_rem:
            ans = seed + 1
            break
        seed += bigger
    print(ans)
