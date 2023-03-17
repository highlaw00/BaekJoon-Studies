import math


def is_prime(n):
    # 소수인지 확인하기 위해서 1부터 루트N 까지 확인
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
temp = n
rev = 0

for i in range(len(str(n))):
    unit = temp % 10
    temp //= 10
    if unit == 3 or unit == 4 or unit == 7:
        print("no")
        exit()
    elif unit == 6 or unit == 9:
        unit = 6 if unit == 9 else 9
    rev = rev * 10 + unit

if is_prime(n) and is_prime(rev):
    print("yes")
else:
    print("no")
