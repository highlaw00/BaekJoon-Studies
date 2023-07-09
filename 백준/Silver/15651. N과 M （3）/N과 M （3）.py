n, m = map(int, input().split())

ans = []
sheet = [i for i in range(n+1)]


def back(cnt):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, n+1):
        ans.append(i)
        back(cnt + 1)
        ans.pop()


back(0)
