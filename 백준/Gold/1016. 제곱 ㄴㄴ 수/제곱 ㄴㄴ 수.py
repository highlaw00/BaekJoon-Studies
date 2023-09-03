import math

minimum, maximum = map(int,input().split())

n = int(math.sqrt(maximum))
table = [1 for _ in range(n+1)]
primes = []

for i in range(2, int(math.sqrt(n)) + 1):
    if table[i] == 1:
        for j in range(i + i, n+1, i):
            table[j] = 0

for i in range(2, n+1):
    if table[i]:
        primes.append(i)

ans_sheet = {i: True for i in range(minimum, maximum +1)}
for prime in primes:
    powed = prime * prime
    if powed >= minimum:
        start = powed
    elif minimum % powed == 0:
        start = minimum
    else:
        start = minimum // powed * powed + powed
    
    for i in range(start, maximum + 1, powed):
        ans_sheet[i] = False

cnt = 0
for v in ans_sheet.values():
    if v:
        cnt += 1

print(cnt)
