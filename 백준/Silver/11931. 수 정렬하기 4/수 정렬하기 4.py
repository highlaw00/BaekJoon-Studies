input = __import__('sys').stdin.readline

n = int(input())
l = []

for _ in range(n):
    tmp = int(input())
    l.append(tmp)
l.sort()

for i in range(len(l)):
    print(l[len(l)-i-1])
