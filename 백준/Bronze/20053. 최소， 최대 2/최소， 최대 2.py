import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    l = list(map(int, input().rstrip().split()))
    min_val = 1_000_000
    max_val = -1_000_000
    for num in l:
        if min_val > num:
            min_val = num
        if num > max_val:
            max_val = num
    print(min_val, max_val)
