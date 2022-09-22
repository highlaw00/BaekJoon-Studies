l = list(map(int, input().split()))
s = int(input())
l.sort(reverse=True)

for i in range(len(l)):
    if l[i] == s:
        if 1 <= i + 1 <= 5:
            r = 'A+'
            break
        elif 6 <= i + 1 <= 15:
            r = 'A0'
            break
        elif 16 <= i + 1 <= 30:
            r = 'B+'
            break
        elif 31 <= i + 1 <= 35:
            r = 'B0'
            break
        elif 36 <= i + 1 <= 45:
            r = 'C+'
            break
        elif 46 <= i + 1 <= 48:
            r = 'C0'
            break
        else:
            r = 'F'
print(r)
