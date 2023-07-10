def f(n):
    if n > 3:
        return f(n-1) + f(n-2) + f(n-3)
    elif n == 3:
        return 4
    elif n == 2:
        return 2
    else:
        return 1


t = int(input())
for _ in range(t):
    n = int(input())
    print(f(n))
