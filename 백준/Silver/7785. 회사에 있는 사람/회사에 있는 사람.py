n = int(input())
D = dict()

for i in range(n):
    log = list(map(str,input().split()))
    D[log[0]] = log[1]
    
l = []
keys = list(D.keys())

for i in range(len(keys)):
    curr_key = keys[i]
    if D[curr_key] == 'enter':
        l.append(curr_key)

l.sort(reverse=True)

for name in l:
    print(name)