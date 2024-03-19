import sys
input = sys.stdin.readline

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)

for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    n = numbers[0]
    summation = 0
    
    for i in range(1, n+1):
        first = numbers[i]
        for j in range(i+1, n+1):
            second = numbers[j]
            summation += gcd(max(first, second), min(first, second))
    
    print(summation)