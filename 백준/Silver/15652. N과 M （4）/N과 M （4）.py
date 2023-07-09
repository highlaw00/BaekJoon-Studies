n, m = map(int, input().split())

ans = []
sheet = [i for i in range(n+1)]


def back(cnt):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return
    minimum = 1 if cnt == 0 else ans[-1]
    for i in range(minimum, n+1):
        ans.append(i)
        back(cnt+1)
        ans.pop()


back(0)
