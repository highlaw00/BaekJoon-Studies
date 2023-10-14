l, r = input().split()
s = input()

keyboards = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]

is_lefts = [
    [True for _ in range(5)] + [False for _ in range(5)],
    [True for _ in range(5)] + [False for _ in range(4)],
    [True for _ in range(4)] + [False for _ in range(3)]
]

locations = {}

for i, keys in enumerate(keyboards):
    for j, key in enumerate(keys):
        locations[key] = (i, j, is_lefts[i][j])

ans = 0

for ch in s:
    x, y, is_left = locations[ch]
    if is_left:
        l_x, l_y, _ = locations[l]
        dist = abs(x - l_x) + abs(y - l_y)
        l = ch
    else:
        r_x, r_y, _ = locations[r]
        dist = abs(x - r_x) + abs(y - r_y)
        r = ch
    ans += 1
    ans += dist

print(ans)
