n = int(input())
ans = 0

for i in range(1, n+1):
    # i에 3, 6, 9가 몇개 들어있는지 카운트
    temp = i
    while temp != 0:
        partial = temp % 10
        if partial == 3 or partial == 6 or partial == 9:
            ans += 1
        temp = temp // 10

print(ans)