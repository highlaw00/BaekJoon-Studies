input = __import__('sys').stdin.readline
n, m = map(int,input().split())
D = dict()

for _ in range(n):
    s, p = map(str,input().rstrip().split())
    D[s] = p

for _ in range(m):
    s = input().rstrip()
    print(D[s])