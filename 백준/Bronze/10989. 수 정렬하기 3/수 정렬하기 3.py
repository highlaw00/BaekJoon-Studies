import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    x = int(input())
    d[x] = d.get(x, 0) + 1
l = list(d.keys())
l.sort()
for num in l:
    count = d[num]
    for _ in range(count):
        print(num)
