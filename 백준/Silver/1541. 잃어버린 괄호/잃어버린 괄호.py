s = input()
l = []
temp = ''

for i in range(len(s)):
    ch = s[i]
    if ch in ('+', '-'):
        l.append(int(temp))
        l.append(ch)
        temp = ''
    else:
        temp += ch
l.append(int(temp))

flag = False
ans = 0
for elem in l:
    if elem == '+':
        continue
    elif elem == '-':
        flag = True
    else:
        # -를 만난 상태
        if flag:
            ans -= elem
        else:
            ans += elem

print(ans)
