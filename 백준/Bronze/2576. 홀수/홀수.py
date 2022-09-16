l = []
for _ in range(7):
    l.append(int(input()))

min = -1
sum = 0

for i in range(7):
    curr = l[i]
    if curr % 2 != 0:
        sum += curr
        if min == -1:
            min = curr
        elif min > curr:
            min = curr

if min == -1:
    print(min)
else:
    print(sum)
    print(min)
