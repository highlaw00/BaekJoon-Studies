a, b = map(int,input().split())
l = []
cnt = 1
sum = 0

for i in range(1,46):
    for j in range(i):
        l.append(i)

for i in range(a-1, b):
    sum += l[i]
    
print(sum) 