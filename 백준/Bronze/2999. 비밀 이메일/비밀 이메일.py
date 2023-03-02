s = input()
n = len(s)
ans = []
r, c = 0, 0

# R,C 결정

for R in range(1, n + 1):
    for C in range(1, n + 1):
        if R <= C and R * C == n and R > r:
            r, c = R, C

# m = R * C
m = list("" for _ in range(c))

for i in range(c):
    sub = s[0:r]
    m[i] = sub
    s = s[r:]

for i in range(r):
    for j in range(c):
        ans.append(m[j][i])

ans = "".join(ans)
print(ans)
