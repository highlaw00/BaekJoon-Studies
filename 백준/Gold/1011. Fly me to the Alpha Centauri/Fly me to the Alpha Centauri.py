import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    x, y = map(int, input().rstrip().split())
    n = y - x
    sq_n = math.sqrt(n)
    gauss_n = int(sq_n)
    if int(sq_n) ** 2 == n:
        print(int(sq_n*2 - 1))
    else:
        if gauss_n * gauss_n < n <= gauss_n * (gauss_n + 1):
            print(gauss_n*2)
        elif gauss_n * (gauss_n + 1) < n <= (gauss_n + 1) * (gauss_n + 1):
            print(gauss_n*2 + 1)
