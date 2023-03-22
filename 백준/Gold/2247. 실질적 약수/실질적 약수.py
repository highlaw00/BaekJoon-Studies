n = int(input())
cnt = 0
for i in range(2, n // 2 + 1):
    cnt += (n // i - 1) * i

if n == 4 or n == 5:
    print(2)
else:
    print(cnt % 1000000)
