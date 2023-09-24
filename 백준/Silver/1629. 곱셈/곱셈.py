def divide(base, exp, div):
    if exp == 1:
        return base % div
    elif exp % 2 == 0:
        half = divide(base, exp // 2, div)
        return half * half % div
    else:
        half = divide(base, exp // 2, div)
        return base % div * half * half % div


a, b, c = map(int, input().split())
print(divide(a, b, c))
