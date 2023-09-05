import sys
input = sys.stdin.readline

n = int(input().rstrip())
names = dict()
l = []

for i in range(n):
    age, name = input().rstrip().split()
    age = int(age)
    names[i] = name
    l.append((age, i))

l.sort(key=lambda x: [x[0], x[1]])

for info in l:
    age, idx = info
    print(age, names[idx])
