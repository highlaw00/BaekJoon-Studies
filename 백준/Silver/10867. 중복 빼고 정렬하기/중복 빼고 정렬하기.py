n = int(input())

S = set()
l = map(int,input().split())

for curr in l:
    S.add(curr)

L = sorted(list(S))
for curr in L:
    print(curr, end = ' ')