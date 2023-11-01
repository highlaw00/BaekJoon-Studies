n, s, m = map(int, input().rstrip().split())

volumes = list(map(int, input().rstrip().split()))
prev = {s}
ans = 0

for vol in volumes:
    temp = set()
    for candidate in prev:
        sub = candidate - vol
        add = candidate + vol
        if 0 <= sub <= m:
            temp.add(sub)
        if 0 <= add <= m:
            temp.add(add)
    prev = temp
    # 가능한 경우가 없을 때 -1 출력
    if not prev:
        ans = -1
        break
    ans = max(prev)

print(ans)
