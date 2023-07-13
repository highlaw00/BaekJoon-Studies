n, k, a, b = map(int, input().split())

plants = [k for _ in range(n)]
ans = 0

while 0 not in plants:
    greedy_idx = plants.index(min(plants))
    for i in range(greedy_idx, greedy_idx + a):
        plants[i] += b
    for i in range(n):
        plants[i] -= 1
    ans += 1

print(ans)
