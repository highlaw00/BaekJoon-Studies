a, b, c, n = map(int, input().split())
flag = 0

for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if a * i + b * j + c * k == n:
                flag = 1

print(flag)
