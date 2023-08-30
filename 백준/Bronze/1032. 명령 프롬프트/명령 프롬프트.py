n = int(input())

strings = [list(input()) for _ in range(n)]
m = len(strings[0])
ans = ''

for i in range(m):
    ch = strings[0][i]
    isQuestion = False
    for j in range(n):
        if strings[j][i] != ch:
            isQuestion = True
            break
    if isQuestion:
        ans += '?'
    else:
        ans += ch

print(ans)
