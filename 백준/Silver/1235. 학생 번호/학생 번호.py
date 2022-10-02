n = int(input())
l = []

for _ in range(n):
    l.append(input()[::-1])

k = 1
while (k < len(l[0])):
    s = set()
    for sen in l:        
        s.add(sen[:k])
    if len(s) == n:
        break
    k += 1
print(k)