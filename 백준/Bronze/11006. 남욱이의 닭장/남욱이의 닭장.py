input = __import__('sys').stdin.readline
t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    u = 2 * m - n
    t = m - u
    print(u, t)