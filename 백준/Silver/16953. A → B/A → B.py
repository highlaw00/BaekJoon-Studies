a, b = map(int, input().split())

ans = 0

while True:
    # a와 b가 같다면 success
    if a == b:
        break
    # b가 0이 된다면 fail
    if b == 0:
        ans = -2
        break

    # b를 2로 나눌 수 있다면 2로 나눠주기
    if b % 2 == 0:
        b = b // 2
        ans += 1
    # b의 일의자리 숫자가 1이라면 -1하고 2로 나눠주기
    elif b % 10 == 1:
        b -= 1
        b = b // 10
        ans += 1
    else:
        ans = -2
        break

print(ans + 1)
