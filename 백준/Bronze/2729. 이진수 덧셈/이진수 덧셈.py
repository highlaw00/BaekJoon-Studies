import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n1, n2 = input().rstrip().split()
    n1, n2 = n1[::-1], n2[::-1]
    max_len = max(len(n1), len(n2))
    exp1, exp2 = [0 for _ in range(
        max_len + 1)], [0 for _ in range(max_len + 1)]
    rem = 0
    res = [0 for _ in range(max_len + 1)]

    for i in range(len(n1)):
        exp1[i] = int(n1[i])
    for i in range(len(n2)):
        exp2[i] = int(n2[i])

    for i in range(max_len + 1):
        x1 = int(n1[i]) if i < len(n1) else 0
        x2 = int(n2[i]) if i < len(n2) else 0
        summation = x1 + x2 + rem
        res[i] = (x1 + x2 + rem) % 2
        rem = 1 if summation // 2 else 0

    first_one_idx = 0
    for i in range(max_len, -1, -1):
        if res[i] == 1:
            first_one_idx = i
            break

    print(''.join(map(str, res[first_one_idx::-1])))
