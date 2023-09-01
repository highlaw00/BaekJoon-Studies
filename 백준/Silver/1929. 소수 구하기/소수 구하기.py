import math

m, n = map(int, input().split())
table = [1 for _ in range(n+1)]
table[0] = 0
table[1] = 0

for i in range(2, int(math.sqrt(n)) + 1):
    if table[i] == 1:
        for j in range(i * i, n+1, i):
            table[j] = 0

for i in range(m, n+1):
    if table[i] == 1:
        print(i)
