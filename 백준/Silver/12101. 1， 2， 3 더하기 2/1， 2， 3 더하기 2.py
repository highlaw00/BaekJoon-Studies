ans = []
sheet = [0, 1, 2, 3]
cnt = 0


def f(n):
    if n == sum(ans):
        # 경우의 수 출력
        global cnt
        global k
        cnt += 1
        if cnt == k:
            print('+'.join(map(str, ans)))
        return
    if n < sum(ans):
        return
    for i in range(1, 4):
        ans.append(i)
        f(n)
        ans.pop()


n, k = map(int, input().split())

f(n)

if cnt < k:
    print(-1)
