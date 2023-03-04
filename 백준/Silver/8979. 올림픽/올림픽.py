n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

g, s, b = 0, 0, 0
for country in arr:
    if country[0] == k:
        g, s, b = country[1], country[2], country[3]

arr.sort(reverse=True, key=lambda x: [x[1], x[2], x[3]])

ans = 1
for country in arr:
    if country[1] == g and country[2] == s and country[3] == b:
        if country[0] == k:
            break
        ans -= 1
    ans += 1

print(ans)
