n, m = map(int,input().split())
listen = set()
seen = set()

for _ in range(n):
    name = input()
    listen.add(name)

for _ in range(m):
    name = input()
    seen.add(name)
    
res = sorted(list(listen & seen))

print(len(res))
for name in res:
    print(name)