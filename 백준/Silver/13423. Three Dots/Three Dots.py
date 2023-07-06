from itertools import combinations as cb
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    dots = list(map(int, sys.stdin.readline().split()))
    dic = {dots[i]: i for i in range(n)}
    combi = cb(dots, 2)
    ans = 0

    for case in combi:
        if case[0] < case[1]:
            x1, x2 = case[0], case[1]
        else:
            x1, x2 = case[1], case[0]

        x3 = 2 * x2 - x1
        if x3 in dic:
            ans += 1

    print(ans)
