# n개로 된 수열 a1, a2, ..., an
# ai + a(i+1) + ... + aj가 M이 되는 경우의 수를 구하라

n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]
s, e = 0, 0
ans = 0
curr = arr[s]

while s <= e and e != n:
    # e가 넘어갈때 이슈... => e != n
    if curr == m:
        ans += 1
        curr -= arr[s]
        s += 1
        e += 1
        curr += arr[e]
    elif curr < m:
        # 합이 부족하면 e를 늘려준다.
        e += 1
        curr += arr[e]
    else:
        # 합이 넘치면 s를 늘려서 전체 합을 줄인다.
        curr -= arr[s]
        s += 1
        if s > e:
            e += 1
            curr += arr[e]

print(ans)
