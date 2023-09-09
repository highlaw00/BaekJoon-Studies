import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().rstrip().split())
    i = (n - 1) // h + 1
    j = (n - 1) % h + 1
    print(str(j) + str(i).zfill(2))
