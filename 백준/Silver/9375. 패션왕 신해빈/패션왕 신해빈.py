import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    d = dict()
    for _ in range(n):
        _, type = input().split()
        d[type] = d.get(type, 0) + 1
    ans = 1
    for _, val in d.items():
        ans *= (val + 1)
    print(ans - 1)
