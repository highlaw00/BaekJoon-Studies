a, b, c, d, e = map(int, input().split())

i = 1

while True:
    cnt = 0
    if i % a == 0:
        cnt += 1
    if i % b == 0:
        cnt += 1
    if i % c == 0:
        cnt += 1
    if i % d == 0:
        cnt += 1
    if i % e == 0:
        cnt += 1

    if cnt >= 3:
        print(i)
        break
    i += 1
