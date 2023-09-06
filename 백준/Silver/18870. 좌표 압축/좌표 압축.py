import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = list(map(int, input().rstrip().split()))
d = dict()
for idx, num in enumerate(sorted(l)):
    if num not in d:
        d[num] = len(d)

for num in l:
    print(d[num], end=' ')
