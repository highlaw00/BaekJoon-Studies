n, m = map(int, input().split())

ans = [0 for _ in range(m)]
check = [False for _ in range(n)]


def back(cnt):
    # 기저 사례
    if cnt == m:
        for num in ans:
            print(num, end=' ')
        print()
        return
    for i in range(n):
        if not check[i]:
            if cnt != 0 and i+1 < ans[cnt-1]:
                continue
            # i번째 숫자가 ans에 없다면
            check[i] = True
            ans[cnt] = i+1
            back(cnt + 1)
            check[i] = False


back(0)
