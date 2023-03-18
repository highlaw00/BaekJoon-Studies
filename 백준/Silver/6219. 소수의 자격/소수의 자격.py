# 에라토스테네스 체 이용해서 소수 배열 선언
primes = [True for _ in range(4000001)]
primes[0], primes[1] = False, False

for i in range(2, 4000001):  # n logn 내에 동작
    for j in range(i * i, 4000001, i):
        primes[j] = False

a, b, d = map(int, input().split())
ans = 0

for i in range(a, b + 1):  # A부터 B까지
    if primes[i]:  # 소수인지 아닌지 확인
        temp = i
        for j in range(len(str(i))):  # D가 포함되는지 확인
            unit = temp % 10
            if unit == d:
                ans += 1
                break
            temp //= 10
print(ans)
