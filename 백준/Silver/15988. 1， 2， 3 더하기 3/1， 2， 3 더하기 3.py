fs = [0, 1, 2, 4]


def f(n):
    return fs[n-1] + fs[n-2] + fs[n-3]


for i in range(4, 1_000_000 + 1):
    curr_f = f(i) % 1_000_000_009
    fs.append(curr_f)

t = int(input())

for _ in range(t):
    n = int(input())
    print(fs[n])
