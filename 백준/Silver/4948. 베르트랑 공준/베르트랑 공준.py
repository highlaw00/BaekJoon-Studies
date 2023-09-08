import math
import sys
input = sys.stdin.readline
MAXIMUM = 123_456 * 2

table = [1 for _ in range(MAXIMUM + 1)]
table[0] = 0
table[1] = 0
prefix = [0 for _ in range(MAXIMUM + 1)]

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(MAXIMUM)) + 1):
    if table[i] == 1:
        for j in range(i*i, len(table), i):
            table[j] = 0

# 소수 개수 누적합
# prefix[i] = 0 ~ i까지의 값

for i in range(1, len(prefix)):
    prefix[i] = prefix[i-1] + table[i]

while True:
    n = int(input())
    if not n:
        break
    print(prefix[2*n] - prefix[n])
