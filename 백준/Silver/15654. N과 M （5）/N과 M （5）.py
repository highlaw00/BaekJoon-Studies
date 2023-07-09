n, m = map(int, input().split())
lis = sorted(list(map(int, input().split())))
written = {e: False for e in lis}
ans = []


def back(cnt):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return
    for k, v in written.items():
        # ans에 작성되지 않았다면
        if not v:
            ans.append(k)
            written[k] = True
            back(cnt+1)
            written[k] = False
            ans.pop()


back(0)
