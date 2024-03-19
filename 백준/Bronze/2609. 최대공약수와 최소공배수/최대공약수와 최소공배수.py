def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

def lcm(a, b):
    return a * b // gcd(max(a, b), min(a, b))
    
n, m = map(int,input().split())
print(gcd(max(n, m), min(n, m)))
print(lcm(n, m))