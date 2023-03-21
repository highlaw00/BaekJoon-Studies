# nCm에 곱해져있는 10^k 중 k를 구하는 문제

n, m = map(int, input().split())


def f(n, k):
    ret = 0
    while n // k != 0:
        n //= k
        ret += n
    return ret

numer = [f(n, 2) - f(m, 2) - f(n - m, 2), f(n, 5) - f(m, 5) - f(n - m, 5)]

print(min(numer[0], numer[1]))
